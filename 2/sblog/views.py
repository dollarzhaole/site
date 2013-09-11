# Create your views here.
from django.shortcuts import render_to_response
from sblog.models import Blog
from sblog.models import Tag
from sblog.forms import TagForm
from sblog.forms import BlogForm
from sblog.models import Author
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import comments
from django.core.context_processors import csrf


def blog_list(request):
    # blogs = Blog.objects.all()
    blogs = parse_blog(Blog.objects.all())
    # for blog in blogs:
    #     if len(blog.content) > 400:
    #         article = blog.content
    #         blog.content = article[0:399]
    return render_to_response("blog_list.html", {"blogs": blogs,
                                                 "cmt_list": blog_show_comment_list(request),
                                                 "tags": blog_tags_list(request),
                                                 "bloglist": newest_blog(blogs),
                                                 },
                              context_instance=RequestContext(request))

def resume(request):
    return render_to_response("resume.html", {}, context_instance=RequestContext(request))


def blog_show(request, id=''):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        raise Http404
    return render_to_response("blog_show.html", {"blog": blog,
                                                 "cmt_list": blog_show_comment_list(request),
                                                 "tags": blog_tags_list(request),
                                                 "bloglist": newest_blog(Blog.objects.all()),
                                                 },
                              context_instance=RequestContext(request))


def blog_filter(request, id=''):
    tags = Tag.objects.all()
    tag = Tag.objects.get(id=id)
    blogs = parse_blog(tag.blog_set.all())
    return render_to_response("blog_filter.html", {"blogs": blogs,
                                                   "cmt_list": blog_show_comment_list(request),
                                                   "tag": tag,
                                                   "tags": tags,
                                                   "bloglist": newest_blog(blogs),
                                                   },
                              context_instance=RequestContext(request)
    )

def blog_show_comment(request, id=''):
    blog = Blog.objects.get(id=id)
    return render_to_response('blog_comments_show.html', {'blog': blog})


def blog_tags_list(request):
    tag_list = Tag.objects.all()
    return tag_list


def parse_blog(blogs):
    for blog in blogs:
        if len(blog.content) > 400:
            article = blog.content
            blog.content = article[0:399]
    return blogs


def newest_blog(blogs):
    if len(blogs) >= 10:
        blogs = blogs[:10]
    return blogs


def blog_show_comment_list(request):
    qs = comments.get_model().objects.filter(
        site__pk=settings.SITE_ID,
        is_public=True,
        is_removed=False,
        )
    if getattr(settings, 'COMMENTS_BANNED_USERS_GROUP', None):
        where = ['user_id NOT IN (SELECT user_id FROM auth_user_groups WHERE group_id = %s)']
        params = [settings.COMMENTS_BANNED_USERS_GROUP]
        qs = qs.extra(where=where, params=params)
    cmt_list = qs.order_by("-submit_date")[:10]
    return cmt_list


# def blog_add(request):
#     if request.method == 'POST':
#         form = BlogForm(request.POST)
#         tag = TagForm(request.POST)
#         if form.is_valid() and tag.is_valid():
#             cd = form.cleaned_data
#             cdtag = tag.cleaned_data
#             tagname = cdtag['tag_name']
#             for taglist in tagname.split():
#                 Tag.objects.get_or_create(tag_name=taglist.strip())
#             title = cd['caption']
#             author = Author.objects.get(id=1)
#             content = cd['content']
#             blog = Blog(caption=title, author=author, content=content)
#             blog.save()
#             for taglist in tagname.split():
#                 blog.tags.add(Tag.objects.get(tag_name=taglist.strip()))
#                 blog.save()
#             id = Blog.objects.order_by('-publish_time')[0].id
#             return HttpResponseRedirect('/blog/%s' % id)
#     else:
#         form = BlogForm()
#         tag = TagForm(initial={'tag_name': 'notags'})
#     return render_to_response('sblog/blog_add.html', {'form': form, 'tag': tag},
#                               context_instance=RequestContext(request))
#
#
# def blog_update(request, id=""):
#     id = id;
#     if request.method == 'POST':
#         form = BlogForm(request.POST)
#         tag = TagForm(request.POST)
#         if form.is_valid() and tag.is_valid():
#             cd = form.cleaned_data
#             cdtag = tag.cleaned_data
#             tagname = cdtag['tag_name']
#             tagnamelist = tagname.split()
#             for taglist in tagnamelist:
#                 Tag.objects.get_or_create(tag_name=taglist.strip())
#             title = cd['caption']
#             content = cd['content']
#             blog = Blog.objects.get(id=id)
#             if blog:
#                 blog.caption = title
#                 blog.content = content
#                 blog.save()
#                 for taglist in tagnamelist:
#                     blog.tags.add(Tag.objects.get(tag_name=taglist.strip()))
#                     blog.save()
#                 tags = blog.tags.all()
#                 for tagname in tags:
#                     tagname = unicode(str(tagname), "utf-8")
#                     if tagname not in tagnamelist:
#                         notag = blog.tags.get(tag_name=tagname)
#                         blog.tags.remove(notag)
#             else:
#                 blog = Blog(caption=blog.caption, content=blog.content)
#                 blog.save()
#                 return HttpResponseRedirect('/blog/%s' % id)
#     else:
#         try:
#             blog = Blog.objects.get(id=id)
#         except Exception:
#             raise Http404
#         form = BlogForm(initial={'caption': blog.caption, 'content': blog.content}, auto_id=False)
#         tags = blog.tags.all()
#         if tags:
#             taginit = ''
#             for x in tags:
#                 taginit += str(x) + ' '
#             tag = TagForm(initial={'tag_name': taginit})
#         else:
#             tag = TagForm()
#     return render_to_response('sblog/blog_add.html', {'blog': blog, 'form': form, 'id': id, 'tag': tag},
#                               context_instance=RequestContext(request))


# def blog_del(request, id=""):
#     try:
#         blog = Blog.objects.get(id=id)
#     except Exception:
#         raise Http404
#     if blog:
#         blog.delete()
#         return HttpResponseRedirect("/sblog/bloglist/")
#     blogs = Blog.objects.all()
#     return render_to_response("blog_list.html", {"blogs": blogs})


