from django.shortcuts import render, redirect, get_object_or_404
from .models import Note


def note_list(request):
    notes = Note.objects.all().order_by("-created_at")
    return render(request, "my_app/note_list.html", {"notes": notes})


def create_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        color = request.POST.get("color")

        Note.objects.create(
            title=title,
            content=content,
            color=color
        )

        return redirect("note_list")

    return render(request, "my_app/note_form.html")


def update_note(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        note.title = request.POST.get("title")
        note.content = request.POST.get("content")
        note.color = request.POST.get("color")
        note.save()

        return redirect("note_list")

    return render(request, "my_app/note_form.html", {"note": note})


def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        note.delete()
        return redirect("note_list")

    return render(request, "my_app/note_confirm_delete.html", {"note": note})

