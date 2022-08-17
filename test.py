condition_param = store_json["condition"]
operators = []

# result_dict = {"union":[{"crm_attribute":3}]}
result_dict = {}
for large_block in condition_param:    
    operators.append(large_block["type"])
    result_dict[large_block["type"]]=[]
    web_trigger_tags_count=0
    web_custom_tags_count=0
    web_mined_tags_count=0
    web_attribute_tags_count=0
    crm_trigger_tags_count=0
    crm_custom_tags_count=0
    crm_mined_tags_count=0
    crm_attribute_tags_count=0
    for small_block in large_block["condition"]:
        if small_block["channelType"]=="web":
            if small_block["label"]=="trigger":
                web_trigger_tags_count+=1            
        elif small_block["channelType"] =="crm":
            if small_block["label"]=="attribute":
                crm_attribute_tags_count+=1
    result_dict[large_block["type"]].append({"web_trigger_tags_count":web_trigger_tags_count})
    result_dict[large_block["type"]].append({"crm_attribute_tags_count":crm_attribute_tags_count})
                        
# print(f"web_tags_count : {web_tags_count}") 
# print(f"crm_tags_count : {crm_tags_count}")  
print(result_dict) 
