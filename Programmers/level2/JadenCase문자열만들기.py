def solution(s):
    answer = ' '

    sources = s.split(" ")
    new_sources = []
    for source in sources:
        if source != "":
            source = source.lower()
            if not source[0].isdigit():
                source = source[0].upper() + source[1:]

        new_sources.append(source)

    return answer.join(new_sources)

if __name__ == "__main__":
    print(solution("ABCDD          a"))