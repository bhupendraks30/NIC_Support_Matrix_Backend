from django.shortcuts import render
from rest_framework.views import APIView,Response
from .models import *
from rest_framework import status
from .serializers import *
from django.http import Http404

# Create your views here.
# class RegesterUSer(APIView):
#     def post(self,request): 
#        try:    
#             count=User.objects.all().filter(email=request.data['email']).count() 
#             if count==0:
#                 User.objects.create(
#                 name=request.data['name'],
#                 email=request.data['email'],
#                 password=request.data['password'],
#                 image=request.FILES.get('image'),
#                 ).save()
#                 isCreated= (User.objects.all().filter(email=request.data['email']).count()==0)
#                 if not isCreated:
#                     return Response({"code":"200","message":"Registration succesfully"})
#                 else:
#                     return Response({"code":"200","message":"Registration failed !"})              
#             else:
#                 return Response({"code":"200","message":"user allready exist"})            
#        except Exception as e:
#            return Response({"error":e})



# add by a
# class RegisterUser(APIView):
#     def post(self, request):
#         try:
#             # Check if the user already exists
#             count = User.objects.filter(email=request.data['email']).count()
#             if count == 0:
#                 # Create a new user
#                 User.objects.create(
#                     full_name=request.data['full_name'],
#                     email=request.data['email'],
#                     mobile_number=request.data['mobile_number'],
#                     gender=request.data['gender'],
#                     state=request.data['state'],
#                     district=request.data['district'],
#                     city=request.data['city'],
#                     address=request.data['address'],
#                     pin_code=request.data['pin_code'],
#                     password=request.data['password'],
#                     image=request.FILES.get('image'),
#                     role=request.data['role']
#                 ).save()

#                 # Check if the user was successfully created
#                 isCreated = User.objects.filter(email=request.data['email']).count() == 1
#                 if isCreated:
#                     return Response({"code": "200", "message": "Registration successful"})
#                 else:
#                     return Response({"code": "200", "message": "Registration failed"})
#             else:
#                 return Response({"code": "200", "message": "User already exists"})
#         except Exception as e:
#             return Response({"error": str(e)})


class RegisterUserAPIView(APIView):
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            print(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'code':'200', 'message':'Registrationn Successful'}, status=status.HTTP_201_CREATED)
            print(serializer.errors)
            return Response({'code':'400', 'message':serializer.errors}, status=200)
        except Exception as e:
            print(str(e))
            return Response({'code':'500',"error": str(e)}, status=200)




# and by a 


class RegisterUserCreateView(APIView):
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                # Save the validated data and create a new user
                serializer.save()
                return Response({"code": "201", "message": "Registration successful"}, status=status.HTTP_201_CREATED)
            # If serializer is not valid, return errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Handle any other exceptions and return 500 error
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetAllProject(APIView):
    def get(self, request):
        try:
            projects = AddProject.objects.all()
            serializer = AddProjectSerializer(projects, many=True)
            return Response({'code':'200','project_details':serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetAllUsers(APIView):
    def get(self, request):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response({'code':'200','user_details':serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SearchProject(APIView):
    def post(self, request):
        try:
            project_id = request.data['id']
            project = AddProject.objects.get(id=project_id)
            print(project_id)
            if not project:
                print('data not found')
                return Response({'code':'400','message':'Project not found'}, status=200)
            serializer = AddProjectSerializer(project)
            print(serializer.data)
            return Response({'code':'200','project_details':serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class UpdateProjectStatus(APIView):
    def post(self, request):
        try:
            project_id = request.data['id']
            project_status = request.data['status']
            project = AddProject.objects.get(id=project_id)
            project.status = project_status
            project.save()
            return Response({'code':'200','message':'Project status updated successfully'}, status=status.HTTP_200)
        except Exception as e:
            print(str(e))
            return Response({"message": str(e)}, status=200)





#add by  a start
class LoginUser(APIView):
    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            
            # Check if user with given email exists
            user = User.objects.filter(email=email).first()
            
            if user:
                # User exists, now check password
                if user.password == password:
                    # Password matches, prepare response
                    userData=User.objects.filter(email=email).values()
                    response_data = {
                        "code": "200",
                        "message": "Login successfully",
                        "user_details": userData
                    }
                    return Response(response_data)
                else:
                    # Password does not match
                    return Response({"code": "400", "message": "Incorrect password"})
            else:
                # User not registered
                return Response({"code": "401", "message": "User not registered"})
        except Exception as e:
            return Response({"code": "500", "message": "Exception occurred", "exception_details": str(e)})
#add by  a end 



# add by a

# class AddProjectCreateAPIView(APIView):
#     def post(self, request):
#         try:
#             serializer = AddProjectSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)       

# add by a



class DeleteUser(APIView):
    def delete(self,request):
        try:
            User.objects.all().filter(id=request.data['id'],email=request.data['email']).delete()
            isDeleted=(User.objects.all().filter(id=request.data['id']).count!=0)
            if isDeleted:
                return Response({"code":"200","message":"User succesfully deleted"})
            else:
                return Response({"code":"500","message":"Something went wrong account is not deleted."})    
        except Exception as e:
            print("error",e)

class UpdatePassword(APIView):
    def post(self, request):
        try:            
            user=User.objects.all().filter(id=request.data['id'],email=request.data['email']).values()
            if not user:
                return Response({"code":"404","message":"User not found",})
            User.objects.all().filter(id=request.data['id'],email=request.data['email']).update(password=request.data['password'])
            return Response({"code":"200","message":"Password succesfully changed"})
        except Exception as e:
            print('error ',e)
            return Response({"code":"500","message":"Some thing went wrong"})



class UpdateProfileImage(APIView):
    def post(self, request):
        print('Request data:', request.data)
        try:
            try:
                user = User.objects.get(id=request.data['id'], email=request.data['email'])
            except User.DoesNotExist:
                return Response({"code": "404", "message": "User not found"})

            if 'image' in request.FILES:
                user.image = request.FILES['image']
                user.save()
                user1 = User.objects.all().filter(id=request.data['id'], email=request.data['email']).values()
                return Response({"code": "200", "message": "Profile successfully changed", "userDetails": user1})
            else:
                return Response({"code": "400", "message": "Image file is missing"})
        
        except Exception as e:
            print('error', e)
            return Response({"code": "500", "message": "Something went wrong"})
        
        

class AddProjectCreateAPIView(APIView):
    def post(self, request):
        print('Request data:', request.data)
        try:
            serializer = AddProjectSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"code": "200", "message": "Project successfully added", 'project_details':serializer.data,}, status=200)
            print('error message is : ',serializer.errors)
            return Response({"code": "500", "message": serializer.errors}, status=200)
        except Exception as e:
            print('Error:', e)
            return Response({"code": "500", "message": "Something went wrong"}, status=200)
    



    def get_object(self, pk):
        try:
            return AddProject.objects.get(pk=pk)
        except AddProject.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            add_project = self.get_object(pk)
            serializer = AddProjectSerializer(add_project)
            return Response(serializer.data)
        except Http404:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            add_project = self.get_object(pk)
            serializer = AddProjectSerializer(add_project, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            add_project = self.get_object(pk)
            add_project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        