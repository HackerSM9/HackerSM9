import pathlib
import re
import os
import datetime
import time
root = pathlib.Path(__file__).parent.resolve()

def replace_chunk(content, marker, chunk, inline=False):
    r = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    if not inline:
        chunk = "\n{}\n".format(chunk)
    chunk = "<!-- {} starts -->{}<!-- {} ends -->".format(marker, chunk, marker)
    return r.sub(chunk, content)

def generateProgressBar(progress, progressBarCapacity = 30):
    passedProgressBarIndex = int(progress * progressBarCapacity)
    progressBar = '▓'*passedProgressBarIndex + '░'*(progressBarCapacity - passedProgressBarIndex)
    return progressBar

if __name__ == "__main__":
    readme = root / "README.md"
    readme_contents = readme.open().read()

    progressBar = "{} \n{} \n⏰ Update on {}\n".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(progressBar)
    rewritten = replace_chunk(readme_contents, "progress", progressBar)

    readme.open("w").write(rewritten)
