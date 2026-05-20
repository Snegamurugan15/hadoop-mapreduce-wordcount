from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.wordcount import count_words


def main():
    text = sys.stdin.read()
    for word, count in count_words(text).most_common():
        print(f"{word}\t{count}")


if __name__ == "__main__":
    main()
