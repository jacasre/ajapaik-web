from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.views import serve
from django.views.generic import RedirectView, TemplateView

from project.ajapaik.bbox_api import PhotosView
from project.ajapaik.sitemaps import PhotoSitemap, StaticViewSitemap
from project.ajapaik import views, api, delfi, bbox_api, then_and_now_tours, juks
import django
import project
from django.contrib.sitemaps.views import sitemap

#from allauth import urls


urlpatterns = [
   url(r'^accounts/', include('allauth.urls')),
   url(r'^stream/', views.fetch_stream),
   url(r'^difficulty-feedback/', views.difficulty_feedback, name="project.ajapaik.views.difficulty_feedback"),
   url(r'^geotag/add/', views.geotag_add, name="project.ajapaik.views.geotag_add"),
   url(r'^geotag/confirm/', views.geotag_confirm, name="project.ajapaik.views.geotag_confirm"),
   url(r'^general-info-modal-content/$', views.get_general_info_modal_content, name='project.ajapaik.views.get_general_info_modal_content'),
   url(r'^info-modal-content/$', views.get_album_info_modal_content, name='project.ajapaik.views.get_album_info_modal_content'),
   url(r'^ajapaikaja/$', views.game, name='project.ajapaik.views.game'),
   url(r'^game/$', views.game, name='project.ajapaik.views.game'),
   url(r'^geotag/$', views.game, name='project.ajapaik.views.game'),
   url(r'^kaart/$', views.mapview, name='project.ajapaik.views.mapview'),
   url(r'^map/$', views.mapview, name='project.ajapaik.views.mapview'),
   url(r'^map/photo/(?P<photo_id>\d+)/$', views.mapview, name='map'),
   url(r'^map/rephoto/(?P<rephoto_id>\d+)/$', views.mapview, name='map'),
   url(r'^map/photo/(?P<photo_id>\d+)/rephoto/(?P<rephoto_id>\d+)/$', views.mapview, name='map'),
   url(r'^map-data/$', views.map_objects_by_bounding_box),
   url(r'^leaderboard/$', views.leaderboard, name='project.ajapaik.views.leaderboard'),
   url(r'^leaderboard/album/(?P<album_id>\d+)/$', views.leaderboard, name='album_leaderboard'),
   url(r'^all-time-leaderboard/$', views.all_time_leaderboard, name='all_time_leaderboard'),
   url(r'^top50/$', views.top50, name='project.ajapaik.views.top50'),
   url(r'^top50/album/(?P<album_id>\d+)/$', views.top50, name='album_top50'),
   url(r'^foto/(?P<photo_id>\d+)/upload/$', views.rephoto_upload),
   url(r'^photo/(?P<photo_id>\d+)/upload/$', views.rephoto_upload),
   url(r'^photo/like/$', views.update_like_state, name="project.ajapaik.views.update_like_state"),
   url(r'^photo-upload-modal/$', views.mapview_photo_upload_modal, name='project.ajapaik.views.mapview_photo_upload_modal'),
   url(r'^photo-upload-modal/(?P<photo_id>\d+)/$', views.mapview_photo_upload_modal),
   url(r'^foto/$', views.photoslug, name='project.ajapaik.views.photoslug'),
   url(r'^foto/(?P<photo_id>\d+)/$', views.photoslug, name="project.ajapaik.views.photoslug"),
   url(r'^foto/(?P<photo_id>\d+)/(?P<pseudo_slug>.*)/$', views.photoslug),
   url(r'^photo/$', views.photoslug),
   url(r'^photo/(?P<photo_id>\d+)/$', views.photoslug),
   url(r'^photo/(?P<photo_id>\d+)/(?P<pseudo_slug>.*)/$', views.photoslug),
   url(r'^video/(?P<video_id>\d+)/(?P<pseudo_slug>.*)/$', views.videoslug),
   url(r'^video-still/$', views.generate_still_from_video),
   # Legacy URLs
   url(r'^foto_thumb/$', views.image_thumb, name='project.ajapaik.views.image_thumb'),
   url(r'^foto_thumb/(?P<photo_id>\d+)/$', views.image_thumb),
   url(r'^foto_thumb/(?P<photo_id>\d+)/(?P<thumb_size>\d+)/', views.image_thumb),
   url(r'^foto_thumb/(?P<photo_id>\d+)/(?P<thumb_size>\d+)/(?P<pseudo_slug>.*)/$', views.image_thumb),
   url(r'^foto_url/(?P<photo_id>\d+)/$', views.image_thumb),
   url(r'^foto_large/(?P<photo_id>\d+)/$', views.image_full),
   url(r'^foto_large/(?P<photo_id>\d+)/(?P<pseudo_slug>.*)/$', views.image_full),
   url(r'^photo-large/(?P<photo_id>\d+)/$', views.image_full),
   url(r'^photo-large/(?P<photo_id>\d+)/(?P<pseudo_slug>.*)/$', views.image_full),
   url(r'^photo-url/(?P<photo_id>\d+)/$', views.image_thumb),
   url(r'^photo-url/(?P<photo_id>\d+)/(?P<pseudo_slug>.*)/$', views.image_thumb),
   # Preferred URLs
   url(r'^photo-thumb/$', views.image_thumb),
   url(r'^photo-thumb/(?P<photo_id>\d+)/$', views.image_thumb),
   url(r'^photo-thumb/(?P<photo_id>\d+)/(?P<thumb_size>\d+)/', views.image_thumb),
   url(r'^photo-thumb/(?P<photo_id>\d+)/(?P<thumb_size>\d+)/(?P<pseudo_slug>.*)/$', views.image_thumb),
   url(r'^photo-full/(?P<photo_id>\d+)/(?P<pseudo_slug>.*)/$', views.image_full),
   url(r'^photo-selection/$', views.photo_selection, name="project.ajapaik.views.photo_selection"),
   url(r'^view-selection/$', views.list_photo_selection, name="list_photo_selection"),
   url(r'^upload-selection/$', views.upload_photo_selection, name="upload_photo_selection"),
   url(r'^$', views.frontpage, name='project.ajapaik.views.frontpage'),
   url(r'^photos/$', views.frontpage, name='frontpage_photos'),
   url(r'^photos/(?P<page>\d+)/$', views.frontpage, name='frontpage_photos'),
   url(r'^photos/(?P<album_id>\d+)/(?P<page>\d+)/$', views.frontpage, name='frontpage_photos'),
   url(r'^frontpage-async/$', views.frontpage_async_data, name='project.ajapaik.views.frontpage_async_data'),
   url(r'^frontpage-async-albums/$', views.frontpage_async_albums, name='project.ajapaik.views.frontpage_async_albums'),
   url(r'^curator/$', views.curator, name='curator'),
   url(r'^curator-album-info/$', views.curator_get_album_info),
   url(r'^curator-update-my-album/$', views.curator_update_my_album),
   url(r'^curator-album-list/$', views.curator_my_album_list),
   url(r'^curator-selectable-albums/$', views.curator_selectable_albums, name='project.ajapaik.views.curator_selectable_albums'),
   url(r'^curator-selectable-parent-albums/$', views.curator_selectable_parent_albums, name='project.ajapaik.views.curator_selectable_parent_albums'),
   url(r'^curator-selectable-parent-albums/(?P<album_id>\d+)/$', views.curator_selectable_parent_albums),
   url(r'^curator-search/$', views.curator_search),
   url(r'^curator-upload/$', views.curator_photo_upload_handler),
   url(r'^public-album-create-handler/$', views.public_add_album, name='public_add_album'),
   url(r'^public-area-create-handler/$', views.public_add_area),
   url(r'^csv-upload/$', views.csv_upload),
   url(r'^norwegian-csv-upload/$', views.norwegian_csv_upload),
   url(r'^uudiskiri/$', views.newsletter, name='newsletter'),
   url(r'^uudiskiri/(?P<slug>.*)/$', views.newsletter),
   url(r'^submit-dating/$', views.submit_dating, name='project.ajapaik.views.submit_dating'),
   url(r'^datings/(?P<photo_id>\d+)/$', views.get_datings),
   url(r'^donate/$', views.donate, name='project.ajapaik.views.donate'),
   url(r'^choose-upload-action/$', views.photo_upload_choice, name='photo_upload_choice'),
   url(r'^user-upload/$', views.user_upload, name='user_upload'),
   url(r'^user-upload-add-album/$', views.user_upload_add_album, name='user_upload_add_album'),
   url(r'^privacy/$', views.privacy, name='privacy'),
   url(r'^terms/$', views.terms, name='terms'),
]
urlpatterns += [
    url(r'^api/v1/login/$', api.Login.as_view()),
    url(r'^api/v1/register/$', api.Register.as_view(), name='api_register'),
    url(r'^api/v1/logout/$', api.api_logout),
    url(r'^api/v1/user/me/$', api.api_user_me),
    url(r'^api/v1/album/nearest/$', api.AlbumNearestPhotos.as_view()),
    url(r'^api/v1/album/state/$', api.AlbumDetails.as_view()),
    url(r'^api/v1/album/photos/search/$', api.PhotosInAlbumSearch.as_view()),
    url(r'^api/v1/album_thumb/(?P<album_id>\d+)/$', api.api_album_thumb),
    url(r'^api/v1/album_thumb/(?P<album_id>\d+)/(?P<thumb_size>.*)/$', api.api_album_thumb),
    url(r'^api/v1/albums/$', api.AlbumList.as_view()),
    url(r'^api/v1/albums/search/$', api.AlbumsSearch.as_view()),
    url(r'^api/v1/photo/upload/$', api.RephotoUpload.as_view(), name='api_photo_upload'),
    url(r'^api/v1/photo/state/$', api.PhotoDetails.as_view()),
    url(r'^api/v1/photo/favorite/set/$', api.ToggleUserFavoritePhoto.as_view()),
    url(r'^api/v1/photos/favorite/order-by-distance-to-location/$', api.UserFavoritePhotoList.as_view()),
    url(r'^api/v1/photos/filtered/rephotographed-by-user/$', api.PhotosWithUserRephotos.as_view()),
    url(r'^api/v1/photos/search/$', api.PhotosSearch.as_view()),
    url(r'^api/v1/photos/search/user-rephotos/$', api.UserRephotosSearch.as_view()),
]

urlpatterns += [
    url(r'^delfi-api/v1/photo/$', delfi.photo_info),
    url(r'^delfi_api/v1/photo/$', delfi.photo_info),
    url(r'^delfi-api/v1/photos-bbox/$', delfi.photos_bbox),
    url(r'^delfi_api/v1/photos_bbox/$', delfi.photos_bbox),
]

urlpatterns += [
    url(r'^bbox/v1/$', PhotosView.as_view())
]

urlpatterns += [
    url(r'^then-and-now-tours/$', then_and_now_tours.frontpage),
    url(r'^then-and-now-tours/create-tour-1/$', then_and_now_tours.create_tour_step_1),
    url(r'^then-and-now-tours/markers-for-step-2/$', then_and_now_tours.get_markers_for_create_step_2),
    url(r'^then-and-now-tours/toggle-photo-selection/$', then_and_now_tours.toggle_photo_selection),
    url(r'^then-and-now-tours/create-tour-2/(?P<tour_id>\d+)/$', then_and_now_tours.create_tour_step_2),
    url(r'^then-and-now-tours/create-tour-3/(?P<tour_id>\d+)/$', then_and_now_tours.create_tour_step_3),
    url(r'^then-and-now-tours/create-tour-4/(?P<tour_id>\d+)/$', then_and_now_tours.create_tour_step_4),
    url(r'^then-and-now-tours/create-tour-5/(?P<tour_id>\d+)/$', then_and_now_tours.create_tour_step_5),
    url(r'^then-and-now-tours/generate-ordered-tour/$', then_and_now_tours.generate_ordered_tour),
    url(r'^then-and-now-tours/map/(?P<tour_id>\d+)/$', then_and_now_tours.map_view),
    url(r'^then-and-now-tours/map/', then_and_now_tours.map_view),
    url(r'^then-and-now-tours/get-map-markers/(?P<tour_id>\d+)/$', then_and_now_tours.get_map_markers),
    url(r'^then-and-now-tours/get-gallery-photos/(?P<tour_id>\d+)/$', then_and_now_tours.get_gallery_photos),
    url(r'^then-and-now-tours/detail/(?P<tour_id>\d+)/(?P<photo_id>\d+)/$', then_and_now_tours.detail),
    url(r'^then-and-now-tours/detail/(?P<tour_id>\d+)/(?P<photo_id>\d+)/(?P<rephoto_id>\d+)/$', then_and_now_tours.detail),
    url(r'^then-and-now-tours/rephoto-thumb/(?P<rephoto_id>\d+)/(?P<thumb_size>\d+)/(?P<pseudo_slug>.*)/$', then_and_now_tours.rephoto_thumb),
    url(r'^then-and-now-tours/rephoto-thumb/(?P<rephoto_id>\d+)/(?P<pseudo_slug>.*)/$', then_and_now_tours.rephoto_thumb),
    url(r'^then-and-now-tours/gallery/(?P<tour_id>\d+)/$', then_and_now_tours.gallery),
    url(r'^then-and-now-tours/camera/upload/$', then_and_now_tours.camera_upload),
    url(r'^then-and-now-tours/tour-complete/(?P<tour_id>\d+)/$', then_and_now_tours.tour_complete),
    url(r'^then-and-now-tours/participants/(?P<tour_id>\d+)/$', then_and_now_tours.participants),
    url(r'^then-and-now-tours/choose-group/(?P<tour_id>\d+)/$', then_and_now_tours.choose_group),
    url(r'^then-and-now-tours/manage/(?P<tour_id>\d+)/$', then_and_now_tours.manage),
    url(r'^then-and-now-tours/settings/(?P<tour_id>\d+)/$', then_and_now_tours.settings),
    url(r'^then-and-now-tours/my-tours/(?P<tour_id>\d+)/$', then_and_now_tours.my_tours),
    url(r'^then-and-now-tours/delete-tour/$', then_and_now_tours.delete_tour),
    url(r'^then-and-now-tours/delete-rephoto/$', then_and_now_tours.delete_rephoto),
    url(r'^then-and-now-tours/toggle-rephoto-open/$', then_and_now_tours.toggle_rephoto_open),
    url(r'^then-and-now-tours/my-tours/$', then_and_now_tours.my_tours),
    url(r'^then-and-now-tours/my-rephotos/(?P<tour_id>\d+)/$', then_and_now_tours.my_rephotos),
    url(r'^then-and-now-tours/send-rephoto-to-ajapaik/(?P<tour_rephoto_id>\d+)/$', then_and_now_tours.send_rephoto_to_ajapaik),
]

urlpatterns += [
    url(r'^juks/empty-json/$', juks.empty_json),
    url(r'^juks/layers/$', juks.layers),
]

sitemaps = {'photo_permalinks': PhotoSitemap, 'static_pages': StaticViewSitemap}

urlpatterns += [
    url(r'^%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), serve, {'show_indexes': True, 'insecure': False}),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^comments/for/(?P<photo_id>\d+)/$', views.CommentList.as_view(), name='comments-for-photo'),
    url(r'^comments/post-one/(?P<photo_id>\d+)/$', login_required(views.PostComment.as_view()), name='comments-post-one'),
    url(r'^comments/delete-one/$', login_required(views.DeleteComment.as_view()), name='comments-delete-one'),
    url(r'^comments/edit-one/$', login_required(views.EditComment.as_view()), name='comments-edit-one'),
    url(r'^comments/like-count/(?P<comment_id>\d+)/$', views.get_comment_like_count, name='comments-like-count'),
    url(r'^comments/', include('django_comments_xtd.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/$', django.views.i18n.javascript_catalog, {'domain': 'djangojs', 'packages': ('project')}, name='django.views.i18n.javascript_catalog'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)),
    url(r'^feed/photos/', RedirectView.as_view(url='http://api.ajapaik.ee/?action=photo&format=atom', permanent=True), name='feed'),
    url(r'^sitemap.xml$', sitemap, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+).xml$', sitemap, {'sitemaps': sitemaps}),
]

handler500 = 'project.ajapaik.views.custom_500'
handler404 = 'project.ajapaik.views.custom_404'
if settings.GOOGLE_ANALYTICS_KEY == 'UA-21689048-1':
    urlpatterns += [url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')), ]
else:
    urlpatterns += [url(r'^robots\.txt$', TemplateView.as_view(template_name='robots-staging.txt', content_type='text/plain')), ]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += [url(r'^media/(.*)', django.views.static.serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}), ]
    urlpatterns += [url(r'^vanalinnad.mooo.com/(.*)', django.views.static.serve, {'document_root': settings.VANALINNAD_ROOT, 'show_indexes': True}), ]
