# Netease-Comment-Spider
没错又是我，我又来了。上次做完了[一言的爬虫](https://github.com/GamerNoTitle/Hitokoto-Spider)以后，我又来做网易云音乐热评的爬虫了！这次爬取的api地址是[https://www.mouse123.cn/api/163/api.php](https://www.mouse123.cn/api/163/api.php)，可以获取到各种参数，可获取到的参数如下表：
<table>
<thead>
<tr>
<th>参数名</th>
<th>含义</th>
</tr>
</thead>
<tbody>
<tr>
<td>song_id</td>
<td>歌曲 ID</td>
</tr>
<tr>
<td>title</td>
<td>歌曲名称</td>
</tr>
<tr>
<td>images</td>
<td>歌曲封面图片，已处理为 https 链接</td>
</tr>
<tr>
<td>author</td>
<td>歌曲作者</td>
</tr>
<tr>
<td>album</td>
<td>歌曲所属专辑</td>
</tr>
<tr>
<td>description</td>
<td>歌曲描述</td>
</tr>
<tr>
<td>pub_date</td>
<td>歌曲发行时间</td>
</tr>
<tr>
<td>comment_id</td>
<td>评论 ID</td>
</tr>
<tr>
<td>comment_user_id</td>
<td>评论所属用户 ID</td>
</tr>
<tr>
<td>comment_nickname</td>
<td>评论所属用户名称</td>
</tr>
<tr>
<td>comment_avatar_url</td>
<td>评论所属用户头像链接，已处理为 https 链接</td>
</tr>
<tr>
<td>comment_content</td>
<td>评论正文</td>
</tr>
<tr>
<td>comment_pub_date</td>
<td>评论发表日期</td>
</tr>
</tbody>
</table>

本次使用的还是python的requests库，使用

```bash
$ pip install requests
```

来进行相关依赖库的安装！

其中csv表格中固定会有

## 配置文件

在config.json可以调整配置，其中可选配置如下：

```json
{
    "path": "Netease.csv",
    "times": 3,
    "delay": 0,
    "timeout": 60,
    "song_id": false,
    "images": false,
    "album": false,
    "description": false,
    "pub_date": false,
    "comment_user_id": false,
    "comment_avatar_url": false,
    "comment_pub_date": false
}
```

``path``为文件输出的路径，文件以csv格式输出，请务必带文件后缀！

``times``为抓取次数，支持大于0的整数，直接输入数字即可！

``delay``表示抓取一次得到结果以后等待的时长，为了不给api提供商造成太大的服务器负担，我强烈建议设置此项，填入大于等于0的整数即可，单位是秒

``timeout``表示连接超时时长，支持大于5的整数

``song_id``为歌曲的id，如果开启将把歌曲id写入csv文档，只支持true或false

``images``表示是否抓取图片，这是专辑封面，将保存到``".\albums"``文件夹并命名为对应的评论ID，只支持true或false

``album``表示歌曲来源专辑，如果开启将把专辑名写入csv文件，只支持true或false

``description``表示歌曲的描述，如果开启将把描述写入csv文件，只支持true或false

``pub_date``表示歌曲发行的时间，如果开启将把时间写入csv文档，格式为``YYYY-MM-DD HH:MM:SS``，只支持true或false

``comment_user_id``表示评论的用户的id，如果开启将把id写入csv文档，只支持true或false

``comment_avatar_url``表示评论用户的头像，如果开启将把头像存瑞``.\avatars``文件夹并命名为对应的评论ID，只支持true或false

``comment_pub_date``表示评论发布的时间，如果开启将把时间写入csv文档，格式为``YYYY-MM-DD HH:MM:SS``，只支持true或false

---

# 开发进程

- [ ] 获取api返回的json
- [ ] 导出为csv文件
- [ ] 自定义输出路径
- [ ] 自定义抓取数
- [ ] 自定义延迟
- [ ] 自定义超时时间
- [ ] 自带将获取到的unicode转换为gbk
- [ ] json文件支持