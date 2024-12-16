import sys

def reverse_file_content(input_path, output_path):
    # ファイルを読み込みモードで開く
    with open(input_path, 'r') as infile:
        # ファイルの内容を読み込む
        content = infile.read()

    # 文字列を逆順にする
    reversed_content = content[::-1]

    # 逆順にした内容を新しいファイルに書き込む
    with open(output_path, 'w') as outfile:
        outfile.write(reversed_content)

def copy_file(input_path, output_path):
    # ファイルを読み込みモードで開く
    with open(input_path, 'r') as infile:
        # ファイルの内容を読み込む
        content = infile.read()
    
    with open(output_path, 'w') as outfile:
        outfile.write(content)

def duplicate_contents(input_path, duplication_count):
    # ファイルを読み込みモードで開く
    with open(input_path, 'r') as infile:
        # ファイルの内容を読み込む
        content = infile.read()

    # 複製された内容を新しいファイルに書き込む
    with open(input_path, 'w') as outfile:
        for i in range(duplication_count):
            outfile.write(content)
    
def replace_string(input_path, needle, newstring):
    # ファイルを読み込みモードで開く
    with open(input_path, 'r') as infile:
        # ファイルの内容を読み込む
        content = infile.read()

    # 文字列を置換する
    replaced_content = content.replace(needle, newstring)

    # 置換された内容を新しいファイルに書き込む
    with open(input_path, 'w') as outfile:
        outfile.write(replaced_content)

def main():
    if len(sys.argv) < 2:
        print("コマンドを指定してください。")
        sys.exit(1)

    command = sys.argv[1]

    if command == "reverse":
        # 引数の確認
        if len(sys.argv) != 4:
            print("reverse inputpath outputpath: inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。")
            sys.exit(1)

        input_path = sys.argv[2]
        output_path = sys.argv[3]

        reverse_file_content(input_path, output_path)

    elif command == "copy":
        # 引数の確認
        if len(sys.argv) != 4:
            print("copy inputpath outputpath: inputpath にあるファイルのコピーを作成し、outputpath として保存します。")
            sys.exit(1)

        input_path = sys.argv[2]
        output_path = sys.argv[3]

        copy_file(input_path,output_path)

    elif command == "duplicate-contents":
        # 引数の確認
        if len(sys.argv) != 4:
            print("duplicate-contents inputpath n: inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。")
            sys.exit(1)

            input_path = sys.argv[2]
            duplication_count = sys.argv[3]

            duplicate_contents(input_path, duplication_count)

    elif command == "replace-string":
        # 引数の確認
        if len(sys.argv) != 5:
            print("replace-string inputpath needle newstring: inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。")
            sys.exit(1)

        input_path = sys.argv[2]
        needle = sys.argv[3]
        newstring = sys.argv[4]

        replace_string(input_path, needle, newstring)

    else:
        print("不明なコマンドです。")
        sys.exit(1)

if __name__ == "__main__":
    main()