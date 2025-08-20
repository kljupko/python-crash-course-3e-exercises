# Refactor the user-matching lines in views.py into functions.

# Helper functions.
def check_topic_owner(topic, request):
    """Make sure the topic belongs to the current user."""
    if topic.owner != request.user:
        raise Http404

# Done.