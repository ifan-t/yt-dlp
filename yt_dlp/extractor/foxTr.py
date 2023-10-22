from .common import InfoExtractor
from ..utils import traverse_obj


class foxTrIE(InfoExtractor):
    # _VALID_URL = r'https://www.fox.com.tr/Yabani/bolum/(?P<id>\d+)'
    _VALID_URL = r'https://www.fox.com.tr/[^/]+/bolum/(?P<id>\d+)'
    _TESTS = [{
        'url': 'https://www.fox.com.tr/Yabani/bolum/5',
        'info_dict': {
            'id': '5',
            'ext': 'mp4',
            'title': 'Salı 20.00 - Yeni Bölüm',
            'description': 'md5:1e6f3970ff8e711c6765ae6de2df10ed'
                    },
    }, {
        'url': 'https://www.fox.com.tr/Adim-Farah/bolum/16',
        'info_dict': {
            'id': '16',
            'ext': 'mp4',
            'title': 'ÇARŞAMBA 20.00 - YENİ BÖLÜM',
            'description': 'md5:abcb3c129cb68dbb6cd304fd33b07e96'
        },
    }]

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)
        subtitles = {}
        subtitles.setdefault('tr', []).append({
                'url': 'https://foxtv-static.ercdn.net/foxtv-subtitle/Yabani/bolumler/5/PDTYABANI5HDRTUK7YASVEUZERISIDDETOLUMSUZDAVRANISLAR.vtt?v=1.5',
            })
    
        return {
            'id': video_id,
            'formats': self._extract_m3u8_formats(self._search_regex(r'source : \'(.*?)\',', webpage, 'm3u8_url'), video_id, m3u8_id='hls') ,
            'title' : self._html_search_regex(r'<h3 class="text-uppercase">(.*?)</h3>', webpage, 'title'),
            'subtitles': subtitles,
            'description': self._search_regex(r'<p[^>]*>\s*([^<]+)\s*</p>', webpage, 'description')
        }
        
