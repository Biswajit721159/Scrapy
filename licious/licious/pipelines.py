# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class LiciousPipeline:
    def process_item(self, item, spider):

        adapter=ItemAdapter(item)
        field_name=adapter.field_names()
        
        for field in field_name:
            if(field=="bookname"):
                value=adapter.get(field)
                adapter[field]=value.replace("\\" , "")
            elif(field=="Description"):
                value=adapter.get(field)
                if value != None and len(value)>100:
                    adapter[field]=value[0:100]
         

        
        return item
