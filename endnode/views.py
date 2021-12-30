from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import EndNodeAddForm
from django.contrib import messages


@login_required(login_url= "accounts:authentication")
def addEndNode(request):
    endnodeForm = EndNodeAddForm(request.POST or None)
    context = {
        "endnodeForm" : endnodeForm
    }

    if endnodeForm.is_valid():
        endnodeModel = endnodeForm.save(commit=False)
        endnodeModel.user = request.user
        endnodeModel.save()
        messages.success(request, "EndNode entry added.")

    return render(request, "endnode/endnode-add.html", context)