# FunnyJSONExplorer
可视化JSON文件
使用命令运行
`python FJE.py -s <style> -i <icon-config file> -f <json file>`
icon配置的json格式应为
```
{
    "leaf": leaf icon,
    "non-leaf": non-leaf icon
}
```

Rect风格涉及到矩阵长度设置，可以通过环境变量 *WIDTH*来设置矩阵长度，不设置时默认是50字符长度
