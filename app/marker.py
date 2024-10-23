import requests
import uuid
import re
import json

def BlackBox(question: str, language: str) -> tuple:
    with requests.Session() as session:
        session.headers.update(
            {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Site': 'none',
                'Accept-Language': 'en-US,en;q=0.9',
                'Sec-Fetch-User': '?1',
                'Connection': 'keep-alive',
                'Sec-Fetch-Mode': 'navigate',
                'Host': 'www.blackbox.ai',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            }
        )
        response = session.get("https://www.blackbox.ai/agent/Pseudofy-AIGeneratorPseudocodeOeIoRQK", allow_redirects=True)
        cookie_string = '; '.join([str(key) + '=' + str(value) for key, value in session.cookies.get_dict().items()])
        data = {
            'messages': [
                {
                'id': 'fx4BICxt_pn2TkusAnbZc',
                'content': f'{question} - {language}',
                'role': 'user'
                }
            ],
            'id': 'fx4BICxt_pn2TkusAnbZc',
            'previewToken': 'null',
            'userId': f'{uuid.uuid4()}',
            'codeModelMode': True,
            'agentMode': {
                'mode': True,
                'id': 'Pseudofy-AIGeneratorPseudocodeOeIoRQK',
                'name': 'Pseudofy - AI Generator Pseudocode'
            },
            'trendingAgentMode': {},
            'isMicMode': False,
            'isChromeExt': False,
            'githubToken': 'null'
        }
        session.headers.update(
            {
                'Referer': 'https://www.blackbox.ai/agent/Pseudofy-AIGeneratorPseudocodeOeIoRQK',
                'Cookie': '{}'.format(cookie_string),
                'Content-Type': 'application/json',
                'Origin': 'https://www.blackbox.ai',
                'Sec-Fetch-Dest': 'empty',
                'Accept': '*/*',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Content-Length': '{}'.format(len(str(data))),
            }
        )
        response2 = session.post("https://www.blackbox.ai/api/chat", data=json.dumps(data), allow_redirects=False)
        if '```' in response2.text:
            response_strings = re.search(r'```(.*?)```', response2.text, re.DOTALL)
            if response_strings:
                return ('success', response_strings.group(1))
            else:
                return ('error', 'No response!')
        elif '<!DOCTYPE html>' in str(response2.text):
            return ('error', 'HTML response!')
        else:
            return ('success', response2.text)