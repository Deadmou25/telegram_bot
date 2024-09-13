import gspread
from gspread.utils import ValueRenderOption

class GooogleWorksheets:
    def __init__(self):
        _CREDENTIALS_FILE = 'credentials.json'
        gc=gspread.service_account(filename='service_account.json')
        sh = gc.open('Передаланное расписание')
        worksheet = sh.sheet1
        self.dictionary = {}
        self.all_data = worksheet.get("U2:AA8", value_render_option=ValueRenderOption.unformatted)
        self.get_students_by_days_of_the_week(self.all_data)

    def get_students_by_days_of_the_week(self,all_data):
        days_of_the_week = ("Пн", "Вт","Ср","Чт","Пт","Сб","Вс")
        self.dictionary = {k:v for k,v in zip(days_of_the_week, all_data)}

    def show_dictionary(self):
        print(self.dictionary)