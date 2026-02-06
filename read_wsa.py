import sys

def read_wsa(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines or not lines[0].startswith("#WSA"):
        return "❌ WSA 파일이 아님"

    text = "".join(lines[1:])
    text = text.replace("^B", "[BOLD]")
    text = text.replace("^b", "[/BOLD]")

    return text


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("파일을 더블클릭해서 실행하세요 (.wsa)")
    else:
        path = sys.argv[1]
        print("WSA 파일:", path)
        print("----- 내용 -----")
        print(read_wsa(path))

    input("\n엔터를 누르면 종료")
