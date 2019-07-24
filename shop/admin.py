from django.contrib import admin
from .models import Category,Product,ProductImage

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name','slug']
	prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

# class ProductAdmin(admin.ModelAdmin):
# 	list_display = ['name','price','stock','available','created','updated']
# 	list_editable = ['price','stock','available']
# 	prepopulated_fields = {'slug':('name',)}
# 	list_per_page = 20
# admin.site.register(Product,ProductAdmin)


class ProductImageAdmin(admin.TabularInline):	
   model = ProductImage	
   fieldsets = [		
              (None,{
                     'fields': ['name', 'image'],
              }),	
   ]	
   max_num = 4  
 
 
class ProductAdmin(admin.ModelAdmin):
   list_display = ['name','price','stock','available','created','updated']	
   list_editable = ['price','stock','available']	
   prepopulated_fields = {'slug':('name',)}	
   list_per_page = 20	
   inlines = [
               ProductImageAdmin,
   ]  
 
admin.site.register(Product,ProductAdmin)