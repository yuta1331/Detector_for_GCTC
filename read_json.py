
##############################################
# for reading json                           #
#  1. read recommendation.json               #
#  2. figuring home_date                     #
##############################################

import json

class Read_json:
  def __init__(self, input_json):
    with open(input_json, 'r') as f:
      self.data = json.load(f)

  def all_data(self):
    return self.data

  def update_count(self):
    return self.data['updatecount']

  def home_date(self):
    params = self.data["params"]
    # params = 'params': {'home_no': '10', 'month': '12', 'year': '2016'}
    
    home_dict = {
      0: '15406293',
      1: '15406309',
      2: '15406316',
      3: '15406330',
      4: '17733380',
      5: '17733403',
      6: '17733441',
      7: '17733458',
      8: '18279306',
      9: '18279337',
      10: '18279344',
      11: '19656977',
      12: '20733902',
      13: '20733933',
      14: '21617911',
      15: '21617959',
      16: '22577115',
      17: '22577122',
      18: '22577153',
      19: '22577177',
      20: '22577191',
      21: '25495058'
    }
    
    home_date = home_dict[int(params["home_no"])] + "_" + params["year"] + "-" + params["month"] + "-" + "30" # "30" は要検討
    # home_date = 20733902_2016-11-30
    return home_date

if __name__ == '__main__':
  read_json = Read_json("config_jsons/recommendation.json")
  print(read_json.all_data())
  print(read_json.update_count())
  print(read_json.home_date())
