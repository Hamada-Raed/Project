from django.urls import path     
from . import views
app_name = 'SM_app'
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup_page, name='signup-page'),
    path('login/', views.signin_page, name='signin-page'),
    path('register', views.register, name='registrProcess'),
    path('loging', views.login, name="loginProcess"),
    path('dashboard/', views.dashboard, name='dashboard'),
#path('dashboard/soon_expired', views.soon_expired, name='dashboard'),
    path('dashboard/profile', views.profile, name='profile'),
    path('dashboard/products', views.prodcuts, name='products-page'),
    path('register', views.register, name='registrProcess'),
    path('loging', views.login, name="loginProcess"),
    path('order_page', views.order_page, name='displayOrderPage'),
    path('dashboard/products/add_new', views.add_product, name='add_product'),
    path('save_product/', views.save_product, name='save_product'),
    path('edit', views.edit, name='edit'),
#Kareem urls
    path('order_page', views.order_page, name="order_page"),
    path('order_list_process', views.order_list_process, name="order_list_process"),
    path('get_order_list', views.get_order_list, name="get_order_list"),
    path('remove_order_list/<int:order_id>', views.remove_order_list, name="remove_order_list"),
#Kareem urls Update2
    path('process_order', views.process_order, name="process_order"),
    path('clear_all_order_list_process', views.clear_all_order_list_process, name="clear_all_order_list_process"),
    path('logout_process', views.logout_process, name="logout_process"),
# Kareem urls Update 3: Dahsboard Remove link
    path('remove_product_process/<int:product_id>', views.remove_product_process, name="remove_product_process"),
    path('display_orders_page', views.display_orders_page, name="display_orders_page"),

############################## Prodcut Part ###############################
    path('display_products/', views.display_products),
    # path('save_products/', views.save_products, name='save_products'),
    path('all_product/', views.all_product), 
    path('product_list_process/', views.product_list_process, name='product_list_process'), 
    path('get_product_list/', views.get_product_list, name='get_product_list'), 
    path('search', views.search),
    path('display_products/remove_product_list/<int:product_id>', views.remove_product_list, name="remove_product_list"),
    path('process_product', views.process_product, name="process_product"),
    path('clear_all_product', views.clear_all_product, name="clear_all_product"),  

######################### reset the password ############################# 
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
 
]
