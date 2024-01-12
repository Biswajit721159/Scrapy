# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FirstprojectPipeline:
    def process_item(self, item, spider):
        adapter=ItemAdapter(item)
        field_name=adapter.field_names()
        
        for field in field_name:
            if(field=="rating"):
                value=adapter.get(field)
                if value==None:
                    adapter[field]='0.0'

        if(adapter.get('offer')==None):
            adapter['offer']='0% OFF'            

        
        return item


