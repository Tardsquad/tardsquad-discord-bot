import re


class TextColor:
    """Hack to get colored strings in Discord.

    Refernce: https://www.streamscheme.com/how-to-change-discord-text-color/
    """

    @staticmethod
    def red(text):
        prefixed = re.sub("^", "- ", text, flags=re.M)
        return "```diff\n{:s}\n```".format(prefixed)

    @staticmethod
    def orange(text):
        return "```css\n[{:s}]\n```".format(text)

    @staticmethod
    def yellow(text):
        return "```fix\n{:s}\n```".format(text)

    @staticmethod
    def green_dark(text):
        return '```bash\n"{:s}"\n```'.format(text)

    @staticmethod
    def green_light(text):
        prefixed = re.sub("^", "+ ", text, flags=re.M)
        return "```diff\n{:s}\n```".format(prefixed)

    @staticmethod
    def blue(text):
        return "```ini\n[{:s}]\n```".format(text)
