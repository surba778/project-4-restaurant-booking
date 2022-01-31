from .models import Reservation
from django.shortcuts import render
from .forms import ReservationForm
from django.views import generic, View


from reservation.models import Reservation

def book_table(request):
    book_form = ReservationForm()

    if request.method == 'POST':
        book_form = ReservationForm(request.POST)

        if book_form.is_valid():
                book_form.save()
                
  
    context = {'form': book_form }
    
    return render(request, 'reservation/book.html', context)    

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                
                "reservation_form": reservationform()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        reservation_form: ReservationForm(data=request.POST)
        if  reservation_form.is_valid():
            reservation_form.instance.email = request.user.email
            reservation_form.instance.name = request.user.username
            reservation = reservation_form.save(commit=False)
            reservation.post = post
            reservation.save()
        else:
            reservation_form: ReservationForm()

        return render(
            request,
            "post_detail.html",
            {
                "reservation_form": reservation_form,
            },
        )

    

