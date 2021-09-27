from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from user_alerts.models import UserAlerts, EbayItems
from utils.ebay import Ebay

class Alert:
    def __init__(self, alert_id):
        self.alert_id = alert_id
        self.alerts = UserAlerts.objects.get(id=self.alert_id)

    def insert_items(self):
        ebay = Ebay()
        search = ebay.search(self.alerts.search_phrase)
        print('================== ', search)
        if search is not None:
            for items in search:
                single_item = ebay.getItem(item_id=items['itemId'], fieldgroups='PRODUCT')
                if single_item is not None:
                    card_item = EbayItems()
                    card_item.user_alert = self.alerts
                    card_item.item_id = single_item['itemId']
                    card_item.title = single_item['title']
                    card_item.category_path = single_item['categoryPath']
                    card_item.image_url = single_item['image']['imageUrl']
                    card_item.item_web_url = single_item['itemWebUrl']
                    card_item.description = single_item['description']
                    card_item.category_id = single_item['categoryId']
                    card_item.buying_options = single_item['buyingOptions'][0]
                    card_item.value = single_item['price']['value']
                    card_item.currency = single_item['price']['currency']
                    card_item.save()

    def send_email(self):
        self.insert_items()
        print("\n _________period_____________  ", self.alerts.period, '\n')
        plaintext = get_template('email.txt')
        htmly = get_template('email.html')

        items = EbayItems.objects.filter(user_alert=self.alerts).order_by('value')
        d = {'search_phrase': self.alerts.search_phrase, 'items': items}
        d1 = {'search_phrase': self.alerts.search_phrase, 'items': items}
        subject, from_email, to = 'Your eBay Alert', 'rman.karimi.1991@gmail.com', self.alerts.email
        text_content = plaintext.render(d)
        html_content = htmly.render(d1)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "html/text")
        msg.send()


def test():
    print('______________________________________')
