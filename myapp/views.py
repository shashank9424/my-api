from cgitb import reset
from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.views import APIView
from . serializer import *
from . models import *
from rest_framework.response import Response
from django.contrib import auth
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

def wellcome():
    return HttpResponse("wellcome to hamar gola ")
#Group view 

class GroupView(APIView):
    authentication_classes = [ JWTAuthentication ]  
    permission_classes = (IsAuthenticated,)

    def get(self,request,pk=None):
        data= request.GET
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if pk:
                if not Group.objects.filter(pk=pk).exists():
                    return Response ('object dose not exists')
                else:
                    snippet = Group.objects.get(pk=pk)
                    post = GroupSerializer(snippet).data
                    return Response(post)
            else:
                if not Product.objects.exists():
                    return Response('Object dose not exist')
                values=Group.objects.all()
                context=[]
                for obj in values:
                    newdata = GroupSerializer(obj).data
                    context.append(newdata)
                return Response(context)
        else:
            return Response ('unauthorized only admin can use this feature')

    def post(self,request):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            datatype = type(data)
            if datatype == list:
                ser = GroupSerializer(data=data,many=True)
            else:    
                ser = GroupSerializer(data=data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
            return Response(ser.errors) 
        else:
            return Response ('unauthorized only admin can use this feature')     
    def delete(self, request,pk):
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not Group.objects.filter(pk=pk).exists():
                return Response ('object dose not exists')
            else:
                snippet = Group.objects.get(pk=pk)
                snippet.delete()
                return Response({'data':"Deleted"})  
        else:
            return Response ('unauthorized only admin can use this feature')  
    def put(self, request,pk):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not Group.objects.filter(pk=pk).exists():
                return Response('data dose not exist')
            course = Group.objects.get(pk=pk)
            ser = GroupSerializer(course,data=data,partial=True)
            if ser.is_valid(raise_exception=True):
                ser.save()
                return Response(('Details updated',ser.data))
            else:
                return Response(ser.errors)   
        else:
            return Response ('unauthorized only admin can use this feature') 
    def patch(self, request,pk):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not Group.objects.filter(pk=pk).exists():
                return Response('data dose not exist')
            course = Group.objects.get(pk=pk)
            ser = GroupSerializer(course,data=data,partial=True)
            if ser.is_valid(raise_exception=True):
                ser.save()
                return Response(('Details updated',ser.data))
            else:
                return Response(ser.errors)   
        else:
            return Response ('unauthorized only admin can use this feature') 
#   Item view      
class ItemView(APIView):
    authentication_classes = [ JWTAuthentication ]  
    permission_classes = (IsAuthenticated,)            
    def get(self,request,pk=None):
        data= request.GET
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if pk :
                if not Item.objects.filter(pk=pk).exists():
                    return Response ('object dose not exists')
                else:
                    snippet = Item.objects.get(pk=pk)
                    post = ItemSerializer(snippet).data
                    return Response(post)
            else:
                if not Item.objects.exists():
                    return Response('Object dose not exist')
                values=Item.objects.all()
                context=[]
                for obj in values:
                    newdata = ItemSerializer(obj).data
                    context.append(newdata)
                return Response(context)
        else:
            return Response ('unauthorized only admin can use this feature')       
    def post(self,request):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            datatype = type(data)
            if datatype == list:
                ser = ItemSerializer(data=data,many=True)
            else:
                ser = ItemSerializer(data=data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
            return Response(ser.errors)  
        else:
            return Response("only admin can post data")      
    def delete(self, request,pk):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not Item.objects.filter(pk=pk).exists():
                return Response ('object dose not exists')
            else:
                snippet = Item.objects.get(pk=pk)
                snippet.delete()
                return Response({'data':"Deleted"})
        else:
            return Response("only admin can delete the data")            
    def put(self, request,pk):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not Item.objects.filter(pk=pk).exists():
                return Response('data dose not exist')
            course = Item.objects.get(pk=pk)
            ser = ItemSerializer(course,data=data,partial=True)
            if ser.is_valid(raise_exception=True):
                ser.save()
                return Response(('Details updated',ser.data))
            else:
                return Response(ser.errors)
        else:
            return Response("only admin can do this not you")            
    def patch(self, request,pk):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not Item.objects.filter(pk=pk).exists():
                return Response('data dose not exist')
            course = Item.objects.get(pk=pk)
            ser = ItemSerializer(course,data=data,partial=True)
            if ser.is_valid(raise_exception=True):
                ser.save()
                return Response(('Details updated',ser.data))
            else:
                return Response(ser.errors)    
        else:
            return Response("unauthorized for this action")

# Assessable_valueView         
class Assessable_valueView(APIView):
    authentication_classes = [ JWTAuthentication ]  
    permission_classes = (IsAuthenticated,)       
    def get(self,request,pk=None):
        data= request.GET
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if pk:
                if not Assessable_value.objects.filter(pk=pk).exists():
                    return Response ('object dose not exists')
                else:
                    snippet = Assessable_value.objects.get(pk=pk)
                    post = Assessable_valueSerializer(snippet).data
                    return Response(post)
            else:
                if not Assessable_value.objects.exists():
                    return Response('Object dose not exist')
                values=Assessable_value.objects.all()
                context=[]
                for obj in values:
                    newdata = Assessable_valueSerializer(obj).data
                    context.append(newdata)
                return Response(context)
        else:
            return Response("not for you")        
    def post(self,request):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            datatype = type(data)

            if datatype == list:
                ser = Assessable_valueSerializer(data=data,many=True)
            else:    
                ser = Assessable_valueSerializer(data=data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
            return Response(ser.errors) 
        else:
            return Response("unauthorized for this action")        
    def delete(self, request,pk):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not Assessable_value.objects.filter(pk=pk).exists():
                return Response ('object dose not exists')
            else:
                snippet = Assessable_value.objects.get(pk=pk)
                snippet.delete()
                return Response({'data':"Deleted"})    
        else:
            return Response("unauthorized for this action")
    def put(self, request,pk):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not Assessable_value.objects.filter(pk=pk).exists():
                return Response('data dose not exist')
            course = Assessable_value.objects.get(pk=pk)
            ser = Assessable_valueSerializer(course,data=data,partial=True)
            if ser.is_valid(raise_exception=True):
                ser.save()
                return Response(('Details updated',ser.data))
            else:
                return Response(ser.errors)    
        else:
            return Response("unauthorized for this action")
    def patch(self, request,pk): 
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not Assessable_value.objects.filter(pk=pk).exists():
                return Response('data dose not exist')
            course = Assessable_value.objects.get(pk=pk)
            ser = Assessable_valueSerializer(course,data=data,partial=True)
            if ser.is_valid(raise_exception=True):
                ser.save()
                return Response(('Details updated',ser.data))
            else:
                return Response(ser.errors)    
        else:
            return Response("unauthorized for this action")

#  Product view

        
         
class ProductView(APIView):   
    authentication_classes = [ JWTAuthentication ]  
    permission_classes = (IsAuthenticated,)    
    def get(self,request,pk=None):
        data= request.GET
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if pk:
                if not Product.objects.filter(pk=pk).exists():
                    return Response ('object dose not exists')
                else:
                    snippet = Product.objects.get(pk=pk)
                    post = ProductSerializer(snippet).data
                    return Response(post)
            else:
                if not Product.objects.exists():
                    return Response('Object dose not exist')
                values=Product.objects.all()
                context=[]
                for obj in values:
                    newdata = ProductSerializer(obj).data
                    context.append(newdata)
                return Response(context)
        else:
            return Response("unauthorized for this action")

    def post(self,request):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            datatype = type(data)

            if datatype == list:
                ser = ProductSerializer(data=data,many=True)
            else:    
                ser = ProductSerializer(data=data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
            return Response(ser.errors)    
        else:
            return Response("unauthorized for this action")
        
    def delete(self, request,pk):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not Product.objects.filter(pk=pk).exists():
                return Response ('object dose not exists')
            else:
                snippet = Product.objects.get(pk=pk)
                snippet.delete()
                return Response({'data':"Deleted"})    
        else:
            return Response("unauthorized for this action")

    def put(self, request,pk):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not Product.objects.filter(pk=pk).exists():
                return Response('data dose not exist')
            course = Product.objects.get(pk=pk)
            ser = ProductSerializer(course,data=data,partial=True)
            if ser.is_valid(raise_exception=True):
                ser.save()
                return Response(('Details updated',ser.data))
            else:
                return Response(ser.errors)    
        else:
            return Response("unauthorized for this action")

    def patch(self, request,pk):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not Product.objects.filter(pk=pk).exists():
                return Response('data dose not exist')
            course = Product.objects.get(pk=pk)
            ser = ProductSerializer(course,data=data,partial=True)
            if ser.is_valid(raise_exception=True):
                ser.save()
                return Response(('Details updated',ser.data))
            else:
                return Response(ser.errors)    
        else:
            return Response("unauthorized for this action")

# Customer view
class CustomerView(APIView):   
    authentication_classes = [ JWTAuthentication ]  
    permission_classes = (IsAuthenticated,)    
    def get(self,request,pk=None):
        data= request.GET 
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if pk:
                if not Customer.objects.filter(pk=pk).exists():
                    return Response ('object dose not exists')
                else:
                    snippet = Customer.objects.get(pk=pk)
                    post = CustomerSerializer(snippet).data
                    return Response(post)
            else:
                if not Customer.objects.exists():
                    return Response('Object dose not exist')
                values=Customer.objects.all()
                context=[]
                for obj in values:
                    newdata = CustomerSerializer(obj).data
                    context.append(newdata)
                return Response(context)
        else:
            return Response("unauthorized for this action")

    def post(self,request):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            datatype = type(data)

            if datatype == list:
                ser = CustomerSerializer(data=data,many=True)
            else:    
                ser = CustomerSerializer(data=data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
            return Response(ser.errors)  
    def delete(self, request,pk):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not Customer.objects.filter(pk=pk).exists():
                return Response ('object dose not exists')
            else:
                snippet = Customer.objects.get(pk=pk)
                snippet.delete()
            return Response({'data':"Deleted"})    
    def put(self, request,pk):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not Customer.objects.filter(pk=pk).exists():
                return Response('data dose not exist')
            course = Customer.objects.get(pk=pk)
            ser = CustomerSerializer(course,data=data,partial=True)
            if ser.is_valid(raise_exception=True):
                ser.save()
                return Response(('Details updated',ser.data))
            else:
                return Response(ser.errors)    
    def patch(self, request,pk):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not Customer.objects.filter(pk=pk).exists():
                return Response('data dose not exist')
            course = Customer.objects.get(pk=pk)
            ser = CustomerSerializer(course,data=data,partial=True)
            if ser.is_valid(raise_exception=True):
                ser.save()
                return Response(('Details updated',ser.data))
            else:
                return Response(ser.errors)    

#        city view        
class CityView(APIView):  
    authentication_classes = [ JWTAuthentication ]  
    permission_classes = (IsAuthenticated,)     
    def get(self,request,pk=None):
        data= request.GET 
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if pk : 
                if not City.objects.filter(pk=pk).exists():
                    return Response ('object dose not exists')
                else:
                    snippet = City.objects.get(pk=pk)
                    post = CitySerializer(snippet).data
                    return Response(post)
            else:
                if not City.objects.exists():
                    return Response('Object dose not exist')
                values=City.objects.all()
                context=[]
                for obj in values:
                    newdata = CitySerializer(obj).data
                    context.append(newdata)
                return Response(context)        
        else:
            return Response("unauthorized for this action")

    def post(self,request):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            datatype = type(data)

            if datatype == list:
                ser = CitySerializer(data=data,many=True)
            else:    
                ser = CitySerializer(data=data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
            return Response(ser.errors)
        else:
            return Response("unauthorized for this action")
    def delete(self, request,pk):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not City.objects.filter(pk=pk).exists():
                return Response ('object dose not exists')
            else:
                snippet = City.objects.get(pk=pk)
                snippet.delete()
                return Response({'data':"Deleted"})    
        else:
            return Response("unauthorized for this action")        
    def put(self, request,pk):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not City.objects.filter(pk=pk).exists():
                return Response('data dose not exist')
            course = City.objects.get(pk=pk)
            ser = CitySerializer(course,data=data,partial=True)
            if ser.is_valid(raise_exception=True):
                ser.save()
                return Response(('Details updated',ser.data))
            else:
                return Response(ser.errors)    
        else:
            return Response("unauthorized for this action")
    def patch(self, request,pk):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not City.objects.filter(pk=pk).exists():
                return Response('data dose not exist')
            course = City.objects.get(pk=pk)
            ser = CitySerializer(course,data=data,partial=True)
            if ser.is_valid(raise_exception=True):
                ser.save()
                return Response(('Details updated',ser.data))
            else:
                return Response(ser.errors)    
        else:
            return Response("unauthorized for this action")
# Country view
class CountryView(APIView): 
    authentication_classes = [ JWTAuthentication ]  
    permission_classes = (IsAuthenticated,)      
    def get(self,request,pk=None):
        data= request.GET 
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if pk:
                if not Country.objects.filter(pk=pk).exists():
                    return Response ('object dose not exists')
                else:
                    snippet = Country.objects.get(pk=pk)
                    post = CountrySerializer(snippet).data
                    return Response(post)
            else:
                if not Country.objects.exists():
                    return Response('Object dose not exist')
                values=Country.objects.all()
                context=[]
                for obj in values:
                    newdata = CountrySerializer(obj).data
                    context.append(newdata)
                return Response(context)
        else:
            return Response("unauthorized for this action")
         
    def post(self,request):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            datatype = type(data)

            if datatype == list:
                ser = CountrySerializer(data=data,many=True)
            else:    
                ser = CountrySerializer(data=data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
            return Response(ser.errors)
        else:
            return Response("unauthorized for this action")
    def delete(self, request,pk):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not Country.objects.filter(pk=pk).exists():
                return Response ('object dose not exists')
            else:
                snippet = Country.objects.get(pk=pk)
                snippet.delete()
            return Response({'data':"Deleted"})    
        else:
            return Response("unauthorized for this action")
    def put(self, request,pk):
        data = request.data
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not Country.objects.filter(pk=pk).exists():
                return Response('data dose not exist')
            course = Country.objects.get(pk=pk)
            ser = CountrySerializer(course,data=data,partial=True)
            if ser.is_valid(raise_exception=True):
                ser.save()
                return Response(('Details updated',ser.data))
            else:
                return Response(ser.errors)    
        else:
            return Response("unauthorized for this action")
    def patch(self, request,pk):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not Country.objects.filter(pk=pk).exists():
                return Response('data dose not exist')
            course = Country.objects.get(pk=pk)
            ser = CountrySerializer(course,data=data,partial=True)
            if ser.is_valid(raise_exception=True):
                ser.save()
                return Response(('Details updated',ser.data))
            else:
                return Response(ser.errors)    
        else:
            return Response("unauthorized for this action")
# State view
    
class StateView(APIView): 
    authentication_classes = [ JWTAuthentication ]  
    permission_classes = (IsAuthenticated,)      
    def get(self,request,pk=None):
        data= request.GET 
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if pk:
                if not State.objects.filter(pk=pk).exists():
                    return Response ('object dose not exists')
                else:
                    snippet = State.objects.get(pk=pk)
                    post = StateSerializer(snippet).data
                    return Response(post)
            else:
                if not State.objects.exists():
                    return Response('Object dose not exist')
                values=State.objects.all()
                context=[]
                for obj in values:
                    newdata = StateSerializer(obj).data
                    context.append(newdata)
                return Response(context)
        else:
            return Response("unauthorized for this action")
    
    def post(self,request):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            datatype = type(data)

            if datatype == list:
                ser = StateSerializer(data=data,many=True)
            else:    
                ser = StateSerializer(data=data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
            return Response(ser.errors)         
        else:
            return Response("unauthorized for this action")
    def delete(self, request,pk):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not State.objects.filter(pk=pk).exists():
                return Response ('object dose not exists')
            else:
                snippet = State.objects.get(pk=pk)
                snippet.delete()
                return Response({'data':"Deleted"})    
        else:
            return Response("unauthorized for this action")
    def put(self, request,pk):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not State.objects.filter(pk=pk).exists():
                return Response('data dose not exist')
            course = State.objects.get(pk=pk)
            ser = StateSerializer(course,data=data,partial=True)
            if ser.is_valid(raise_exception=True):
                ser.save()
                return Response(('Details updated',ser.data))
            else:
                return Response(ser.errors)    
        else:
            return Response("unauthorized for this action")
    def patch(self, request,pk):
        data = request.data
     
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not State.objects.filter(pk=pk).exists():
                return Response('data dose not exist')
            course = State.objects.get(pk=pk)
            ser = StateSerializer(course,data=data,partial=True)
            if ser.is_valid(raise_exception=True):
                ser.save()
                return Response(('Details updated',ser.data))
            else:
                return Response(ser.errors)    
        else:
            return Response("unauthorized for this action")
# tax  view
class TaxView(APIView):  
    authentication_classes = [ JWTAuthentication ]  
    permission_classes = (IsAuthenticated,)     
    def get(self,request,pk=None):
        data= request.GET 
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if pk:
                if not Tax.objects.filter(pk=pk).exists():
                    return Response ('object dose not exists')
                else:
                    snippet = Tax.objects.get(pk=pk)
                    post = TaxSerializer(snippet).data
                    return Response(post)
            else:
                if not Tax.objects.exists():
                    return Response('Object dose not exist')
                values=Tax.objects.all()
                context=[]
                for obj in values:
                    newdata =TaxSerializer(obj).data
                    context.append(newdata)
                return Response(context)
        else:
            return Response("unauthorized for this action")
        
    def post(self,request):

        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            datatype = type(data)

            if datatype == list:
                ser = TaxSerializer(data=data,many=True)
            else:    
                ser = TaxSerializer(data=data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
            return Response(ser.errors)         
        else:
            return Response("unauthorized for this action")
    def delete(self, request,pk):
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not Tax.objects.filter(pk=pk).exists():
                return Response ('object dose not exists')
            else:
                snippet = Tax.objects.get(pk=pk)
                snippet.delete()
                return Response({'data':"Deleted"})    
        else:
            return Response("unauthorized for this action")
    def put(self, request,pk):
      
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not Tax.objects.filter(pk=pk).exists():
                return Response('data dose not exist')
            course = Tax.objects.get(pk=pk)
            ser =TaxSerializer(course,data=data,partial=True)
            if ser.is_valid(raise_exception=True):
                ser.save()
                return Response(('Details updated',ser.data))
            else:
                return Response(ser.errors)    
        else:
            return Response("unauthorized for this action")
    def patch(self, request,pk):
        
        data = request.data
        user = request.user
        user_status = user.is_superuser
        if user_status:
            if not Tax.objects.filter(pk=pk).exists():
                return Response('data dose not exist')
            course = Tax.objects.get(pk=pk)
            ser = TaxSerializer(course,data=data,partial=True)
            if ser.is_valid(raise_exception=True):
                ser.save()
                return Response({'status' :200,'message':'Details updated','data':ser.data})
            else:
                return Response(ser.errors)    
        else:
            return Response("unauthorized for this action")
                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> login view <<<<<<<<<<<<<<<<<<<<<<<<