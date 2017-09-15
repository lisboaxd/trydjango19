
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post
from .forms import PostForm


# Create your views here.
def posts_list(request):
	queryset_list = Post.objects.all().order_by('-created')
	paginator = Paginator(queryset_list,5)

	page = request.GET.get('pagina')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		'title':'Lista',
		'posts':queryset
	}
	return render(request,'base.html',context)

def posts_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,'Post Criado com sucesso', extra_tags='msg-success')
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request,'Erro ao criar Post')
	context = {
		'form':form,
		'title':'Create'
	}
	return render(request,'post_form.html',context)

def posts_delete(request,id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, 'Post Criado com sucesso', extra_tags='msg-success')
	return redirect('posts:list')

def posts_update(request,id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, 'Post editado com sucesso', extra_tags='msg-success')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		'form':form,
		'title':'Editar',
		'instance':instance
	}
	return render(request,'post_form.html',context)

def posts_detail(request,id=None):
	instance = get_object_or_404(Post,id=id)
	context = {
	'post':instance
	}
	return render(request,'post_detail.html',context)