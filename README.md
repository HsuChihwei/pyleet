## 项目介绍
这里包含如下三件法宝：
- Python版本的各种算法实现
- Leetcode刷题最佳实践
- LeetCode刷题自动统计程序
### LeetCode自动统计--介绍
可自动统计最近提交通过的题目, 并以Markdown的形式展示相关的数据。
根据个人需求, 这里重点获取**提交次数**和**重刷次数**这两个指标, 目的是为了更好地辅助做题。
### 使用教程
1. Fork本仓库
2. 配置GitHub Actions所需的参数
    - 点击仓库下的`Settings->Secrets->New repository secret`, 分别添加以下secret
        - Name:`LEETCODE_EMAIL`  Value:你的LeetCode账号
        - Name:`LEETCODE_PASSWORD`  Value:你的LeetCode密码
    - 点击[tokens](https://github.com/settings/tokens)->Generate new token
        - Note:GITHUB_TOKEN
        - Select scopes:建议全部勾选
    - 修改[leet_stat.yml](.github/workflows/leet_stat.yml)文件的`git config --global user.email`, 将`email`更改为你的GitHub邮箱地址
    - 修改[leet_stat.yml](.github/workflows/leet_stat.yml)文件的`git config --global user.name`, 将`name`更改为你的GitHub用户名
3. 默认配置为12小时更新一次，可根据需求修改[action.yml](.github/workflows/leet_stat.yml)文件的`on.schedule.cron`
## 补充说明
如有其他需求, 欢迎提交PR。


> 重刷次数的计算规则为: 累计所有提交通过且互为不同一天的记录次数

> Updated:2021-04-18

| 最近提交时间 | 题目 | 题目难度 | 提交次数 | 通过次数 | 重刷次数 | 通过率 | 最佳实践 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 2021-02-19 09:59 | [#26 删除有序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array) | EASY | 8 | 8 | 1 | 100.0% | [2021-02-19](https://leetcode-cn.com/submissions/detail/146823997/) |
| 2021-02-18 13:08 | [#21 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists) | EASY | 4 | 4 | 1 | 100.0% | [2021-02-18](https://leetcode-cn.com/submissions/detail/146588166/) |
| 2021-02-18 09:31 | [#20 有效的括号](https://leetcode-cn.com/problems/valid-parentheses) | EASY | 11 | 11 | 1 | 100.0% | [2021-02-18](https://leetcode-cn.com/submissions/detail/146534074/) |
| 2021-02-18 08:40 | [#14 最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix) | EASY | 9 | 9 | 1 | 100.0% | [2021-02-18](https://leetcode-cn.com/submissions/detail/146516727/) |
| 2021-02-18 07:48 | [#13 罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer) | EASY | 9 | 9 | 1 | 100.0% | [2021-02-18](https://leetcode-cn.com/submissions/detail/146498752/) |
| 2021-02-18 07:02 | [#9 回文数](https://leetcode-cn.com/problems/palindrome-number) | EASY | 5 | 5 | 1 | 100.0% | [2021-02-18](https://leetcode-cn.com/submissions/detail/146483127/) |
| 2021-02-09 13:05 | [#7 整数反转](https://leetcode-cn.com/problems/reverse-integer) | EASY | 10 | 8 | 1 | 80.0% | [2021-02-09](https://leetcode-cn.com/submissions/detail/144995327/) |
| 2021-02-08 12:45 | [#1 两数之和](https://leetcode-cn.com/problems/two-sum) | EASY | 12 | 8 | 1 | 66.67% | [2021-02-08](https://leetcode-cn.com/submissions/detail/144761415/) |
