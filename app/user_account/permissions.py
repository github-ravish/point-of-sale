from django.http import Http404


class SameUserOnlyMixin(object):

    def has_permissions(self):
        # Assumes that your Ticket model has a foreign key called user.
        return self.get_object().user == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404('You do not have permission.')
        return super(SameUserOnlyMixin, self).dispatch(
            request, *args, **kwargs)