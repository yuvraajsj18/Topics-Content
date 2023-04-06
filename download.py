import requests

def download_image(url, save_path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Cookie': '_csrf=anIx5vUoo0i1IDuWxmN19l0j; locale=en-GB; indent_type=space; space_units=4; keymap=sublime; loginstate=true; userid=47858ac0-9113-4b42-8072-76ab0ca372c2; announcement=feature-preview-overview; io=xUUKWtgnO9zfb-yaCTIk; AWSALB=FVREqEqqcVrKzx7FpLybgOrQbRB060PvigLmPMIxzpKCFUfST2QpB3ES+wwe0A4M+SEnCeS+DUGOM0c8bXWb6IqYrm6sFZAD8gcc99ch9AEm/0XLT9/YCtAu3qLt; AWSALBCORS=FVREqEqqcVrKzx7FpLybgOrQbRB060PvigLmPMIxzpKCFUfST2QpB3ES+wwe0A4M+SEnCeS+DUGOM0c8bXWb6IqYrm6sFZAD8gcc99ch9AEm/0XLT9/YCtAu3qLt; connect.sid=s%3A9WLCphxwvzwHzu0KK69CXJJVjBTNvUpo.i2o5qhNXNeRrSkfpqGO9xXlA%2BQFIi7%2F8ujp5utIk7HQ; aws-waf-token=fcf9f43b-d494-44a8-8806-da20c50d9457:AQoAb0J6FCMAAAAA:IKHJw6uMgiVv28K+jSDIvOhi86lqbBNEzyDNABqaA+/HEiYFHav/A9aIfat58t+g6VLRvgnWH9fwOuBCee1maHzi3al277ggYnyt2vVyaCvCqlje+H6UtjI6ZKEZso4iP+AJK3ahUgSmpVQxTaZcbv/YDBn51E/V1f9CQUh0DLIZhXqaBw/iPQ==',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
    }

    response = requests.get(url, stream=True, headers=headers)
    response.raise_for_status()

    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

image_url = 'https://hackmd.io/_uploads/rkXdnOhbn.png'
save_path = 'image.png'

download_image(image_url, save_path)
