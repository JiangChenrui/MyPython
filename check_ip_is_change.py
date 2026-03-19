# -*- coding: utf-8 -*-
import sys
import time
import os
import socket
import logging
from email.mime.multipart import MIMEMultipart  # 打包多个部分的邮件内容（正文、附件、图片...）
from email.mime.text import MIMEText  # 邮件的正文内容
from email.mime.application import MIMEApplication  # 用来发送附件
from email.mime.image import MIMEImage  # 用来发送图片
import smtplib  # 发送邮件
from email.utils import parseaddr, formataddr
from email.header import Header
from datetime import datetime

# 配置日志：同时输出到控制台和文件，格式带时间戳
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.StreamHandler(),  # 输出到控制台（nohup 重定向到 check_ip.log）
    ]
)
logger = logging.getLogger(__name__)
DOMAIN = 'jcrnas.top'  # 要监控的域名


class EmailAlert(object):

    IP_FILE = 'last_ip.txt'  # 保存上次IP的文件

    def __init__(self):
        """连接smtp服务器"""
        # 1.邮箱服务地址
        smtp_server = 'smtp.163.com'  # 网易邮箱服务地址:smtp.163.com;QQ邮箱服务地址:smtp.qq.com
        # 2.实例化smtplib模块中的SMTP对象
        self.server = smtplib.SMTP()
        # 3.连接服务器，需要2个参数[邮箱服务地址、SMTP端口号]
        self.server.connect(smtp_server, 25)
        # 1.发件人地址
        self.from_addr = '18911671182@163.com'
        # 2.邮箱授权密码 【注意】该密码不是你邮箱的登录密码
        self.password = 'ZAU6X43KTDaxxkSZ'  # 替换成自己的邮箱授权密码
        # 3.收件人地址
        self.send_addr = '1102592323@qq.com'
        # 4.登录邮箱
        self.server.login(self.from_addr, self.password)

    def get_public_ip(self):
        """查询 jcrnas.top 域名对应的 IP"""
        try:
            return socket.gethostbyname(DOMAIN)
        except socket.gaierror as e:
            logger.error(f"域名 {DOMAIN} 解析失败: {e}")
            return None

    def get_last_ip(self):
        """从文件读取上次保存的IP"""
        if os.path.exists(self.IP_FILE):
            with open(self.IP_FILE, 'r') as f:
                return f.read().strip()
        return None

    def save_ip(self, ip):
        """保存IP到文件"""
        with open(self.IP_FILE, 'w') as f:
            f.write(ip)

    def _ensure_connection(self):
        """确保SMTP连接有效，如无效则重新连接"""
        try:
            # 尝试发送空数据检查连接状态
            self.server.noop()[0] == 250
        except:
            # 连接已失效，重新连接
            smtp_server = 'smtp.163.com'
            self.server = smtplib.SMTP()
            self.server.connect(smtp_server, 25)
            self.server.login(self.from_addr, self.password)
            logger.info("SMTP已重新连接")

    def send_email(self, old_ip, new_ip):
        """发送IP变化通知邮件"""
        try:
            # 确保连接有效
            self._ensure_connection()
            # 创建邮件对象
            msg = MIMEMultipart()
            msg['From'] = formataddr(('IP监控系统', self.from_addr))
            msg['To'] = formataddr(('用户', self.send_addr))
            msg['Subject'] = Header('公网IP地址变化通知', 'utf-8').encode()

            # 邮件正文
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            content = f"""
            <html>
            <body>
                <h2>公网IP地址变化通知</h2>
                <p><strong>检测时间：</strong>{current_time}</p>
                <p><strong>原IP地址：</strong>{old_ip or '首次检测'}</p>
                <p><strong>新IP地址：</strong>{new_ip}</p>
                <hr>
                <p style="color: gray;">此邮件由IP监控系统自动发送</p>
            </body>
            </html>
            """
            msg.attach(MIMEText(content, 'html', 'utf-8'))

            # 发送邮件
            self.server.sendmail(self.from_addr, [self.send_addr], msg.as_string())
            logger.info(f"邮件发送成功: {old_ip} -> {new_ip}")
            return True
        except Exception as e:
            logger.error(f"邮件发送失败: {e}")
            return False

    def check_ip_is_change(self):
        """检查IP是否变化，如果变化则发送邮件"""
        current_ip = self.get_public_ip()

        if current_ip is None:
            logger.error("无法获取当前公网IP")
            return False

        last_ip = self.get_last_ip()

        if last_ip is None:
            # 首次运行，保存当前IP
            logger.info(f"首次检测，当前IP: {current_ip}")
            self.save_ip(current_ip)
            self.send_email(None, current_ip)
            return True

        if current_ip != last_ip:
            # IP发生变化
            logger.warning(f"IP已变化: {last_ip} -> {current_ip}")
            self.send_email(last_ip, current_ip)
            self.save_ip(current_ip)
            return True
        else:
            logger.info(f"IP未变化: {current_ip}")
            return False

    def close(self):
        """关闭SMTP连接"""
        try:
            self.server.quit()
        except:
            pass


if __name__ == '__main__':
    try:
        email_alert = EmailAlert()

        # 检查IP变化
        # email_alert.check_ip_is_change()

        # 如果需要持续监控，可以添加循环
        while True:
            email_alert.check_ip_is_change()
            time.sleep(600)  # 每5分钟检查一次

    except KeyboardInterrupt:
        logger.info("程序已停止")
    except Exception as e:
        logger.exception(f"程序运行出错: {e}")
    finally:
        if 'email_alert' in locals():
            email_alert.close()
