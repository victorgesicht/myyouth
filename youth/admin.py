from django.contrib import admin
from.models import book, podcast, chess_awards, work_experience, general_info
# Register your models here.


admin.site.register(book)
admin.site.register(podcast)
admin.site.register(chess_awards)
admin.site.register(work_experience)
admin.site.register(general_info)
