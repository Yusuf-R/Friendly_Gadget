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
# user_data = {"Gaming":"LowEnd"}

# matching_objects = []

# for summary in storage.all(Summary).values():
#   obj_dict = summary.to_dict()

#   # Check if all key-value pairs in user_data are present in obj_dict
#   if all(obj_dict.get(key) == value for key, value in user_data.items()):
#     matching_objects.append(summary)

# print(matching_objects)    
# for i in matching_objects:
#   clx = i.get("__class__")
#   j = (eval(clx))
#   print(dir(j))
  


# obj_dict = []
# data = [i.to_dict() for i in storage.all(Summary).values()]
# matching_results = []
# # Iterate through the data
# matching_results = [item for item in data if all(item.get(key) == value for key, value in user_data.items())]
# print(matching_results)

# dx = storage.all(Summary).values()
# dx_list = []
# for i in dx:
#   j = i.to_dict()
#   for p, k in j.items():
#     flag = True
#     for key, value in user_data.items():
#       if key in j and j[key] == value:
#         flag = True
#       else:
#         flag = False
#         break
#     if flag:
#       dx_list.append(i)
#       break
# print(dx_list)

  
# print(obj_list)
#print(all_obj)

# for k in all_obj:
#   print(k)
#   for g in obj:
#     is_match = True
#     for keys, values in q_fields.items():
#       if keys not in obj and obj[g] != values:
#         is_match = False
#     if is_match:
#       obj_list.append(k)
# print(obj_list)
  # print(summary.model_id)
  # obj = i.to_dict().items()
  # k = summary.models.id
  # print(k)

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



# obj_list = []
# user_data = request.get_json()
# all_obj = storage.all(Summary).values()
# for obj in all_obj:
#     obj_dict = obj.to_dict()
#     for key, value in obj_dict.items():
#         flag = True
#         for k, v in user_data.items():
#             if k in obj_dict and obj_dict[k] == v:
#                 flag = True
#             else:
#                 flag = False
#                 break
#         if flag:
#             obj_list.append(obj)
#             break
# return redirect(url_for('result', result= obj_list), code=302)



m = storage.get(Model, "ef39645b-212e-4a8b-b34e-1d491ad4ae62")
print(m.brands.brand_name)
# for n in m:
#   print(n.model_name)