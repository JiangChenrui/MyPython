#!/bin/bash

export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"

cd $(dirname $0)

# 暂存所有更改
git add .

# 检查是否有更改需要提交
if git diff --cached --quiet; then
    echo "没有更改需要提交"
    exit 0
fi

# 使用 Claude 生成 commit message
COMMIT_MSG=$(claude --print "分析以下 git diff 并生成一个简洁的中文 commit message（只输出 commit message，不要其他内容）：
$(git diff --cached --stat)
$(git diff --cached)")

# 如果 Claude 生成失败，使用日期作为备用
if [ -z "$COMMIT_MSG" ]; then
    COMMIT_MSG="$(date)"
fi

git commit -m "$COMMIT_MSG" &&
git pull --rebase &&
git push
