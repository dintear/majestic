from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return ['majestic:homepage',
                'majestic:about',
                'majestic:vyshivka-na-kroe',
                'majestic:shevrony-i-nashivki',
                'majestic:vyshivka-na-gotovyh-izdeliyah',
                'majestic:cerkovnaya-vyshivka',
                'majestic:cost',
                'majestic:contacts',
                'majestic:qna',]

    def location(self, item):
        return reverse(item)