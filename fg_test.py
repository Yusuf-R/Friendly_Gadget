#!/usr/bin/env python3
"""The blueprint for all CRUD operation for Brand."""
from models.brand import Brand
from models.model import Model
from models.summary import Summary
from models import storage


# brands = storage.all(Brand).values()
# id = "ef39645b-212e-4a8b-b34e-1d491ad4ae62"
# models = storage.get(Model, id)
# # print(models.model_name)
# # print(models.model_img)
# # print()
# # print()
all_obj = storage.all(Summary).values()
for summary in all_obj:
  # print(summary.model_id)
  # obj = i.to_dict().items()
  k = summary.models.id
  print(k)
  
  # print(k.model_name)
  # print(k.model_img)
  # j = k.brands
  # print(j.brand_name)
  # for key, val in obj:
  #   # if key in ["id", "__class__", "model_id"]:
  #   #   continue
  #   print(key, val)
  # print()
  
  


# we know we can get the features of this exact brand

# try:
#   f = models.features
#   print("Success")
# except Exception:
#   print("Error")
# for i in f:
#   obj_dict = i.to_dict()
#   new_dict = {}
#   for k, v in obj_dict.items():
#     if k in  ["id", "__class__", "model_id"]:
#       continue
#     for g, h in v.items():
#       print(g, h)


# brand_name.append(obj.brand_name)
# if obj.brand_name == "Apple":
# apple_obj = obj
# for models in apple_obj.models:
# apple_list.append(models.model_name)
# all_model_list.append(models.model_img)
# elif obj.brand_name == "Samsung":
# samsung_obj = obj
# for models in samsung_obj.models:
# samsung_list.append(models.model_name)
# samsung_list.append(models.model_img)
# elif obj.brand_name == "Huawei":
# huawei_obj = obj
# for models in huawei_obj.models:
# huawei_list.append(models.model_name)
# huawei_list.append(models.model_img)
# brand_name = sorted(brand_name)

