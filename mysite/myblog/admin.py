from django.contrib import admin
from myblog.models import Post, Category

admin.site.register(Post)
admin.site.register(Category)


#class CategoriesInline(admin.TabularInline):
#    model = Category
#
#class PostAdmin(admin.ModelAdmin):
#    inlines = [CategoriesInline,]
#admin.site.register(Post, PostAdmin)
#
#
#class CategoryAdmin(admin.ModelAdmin):
#    exclude = ('posts',)
#admin.site.register(Category, CategoryAdmin)


