from django import template

register=template.Library()
@register.filter(name='chunks')
def chunks(list_data,chunks_size):
    chunks=[]
    i=0
    for data in list_data:
        chunks.append(data)
        i=i+1
        if i == chunks_size:
            yield chunks
            i=0
            chunks=[]
    if chunks:
        yield chunks
