# xtaste

1. 环境 python3.6
2. git clone git@github.com:fitnesses/xtaste.git
3. 安装依赖 pip install -r requirements.txt
4. 将英文字典文件excel放到train_folder中，待翻译的excel文件放到translate_folder中
5. 执行
    
    ```bash
    python --train /path/to/train_folder --translate /path/to/translate_folder
    ```
6. 上述命令直接会直接在控制台输出结果，如果需要保存到文件中，可以使用重定向

    ```bash
    python --train /path/to/train_folder --translate /path/to/translate_folder >> result_file
    ```


