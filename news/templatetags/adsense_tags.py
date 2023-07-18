from django import template
from django.template.loader import render_to_string
import re

register = template.Library()


@register.filter
def inject_adsense_after_paragraph(value, arg):
    # Render our adsense code placed in html file
    ad_code = render_to_string("news/detail/adsense_ads.html")

    # Break down content into paragraphs
    if '!reklama' not in value:
        paragraphs = value.split("</p>")
    # Check if paragraph we want to post after exists
        if arg < len(paragraphs):

        # Append our code before the following paragraph
            paragraphs[arg] = ad_code + paragraphs[arg]

        # Assemble our text back with injected adsense code
            value = "</p>".join(paragraphs)

    if '!reklama' in value:
        value = value.replace('!reklama', ad_code)
    if '!twitter' in value:
        result = re.finditer('!twitter(.*)!twitter', value)
        elo = []
        for r in list(result):
            start = r.start()
            end = r.end()
            tweet = value[start:end]
            tweet_after = str(value[start+8:end-8]).\
                replace('&lt;', '<')\
                .replace('&gt;', '>').\
                replace('&amp;amp;', '&amp;').\
                replace('&amp;mdash;', '&mdash;')
            elo.append([tweet, tweet_after])
        for e in elo:
            value = value.replace(e[0], e[1])
            value = value.replace('class="twitter-tweet">', 'class="twitter-tweet"; style="margin:auto>"')
    return value