from django import template

register = template.Library()


@register.assignment_tag(takes_context=True)
def get_thumbnail_size(context, image):
    """
    Returns a string representing the size of the thumbnail, suitable
    for easy-thumbnail, eg.: '150x0', '0x200', '200x200', etc.
    """
    if not image or not context['CONFIG']['THUMBNAIL_ENABLED']:
        return False
    if context['CONFIG']['THUMBNAIL_PRESERVE_RATIO']:
        if image.height > image.width:
            ret = '0x%s' % context['CONFIG']['THUMBNAIL_MAX_HEIGHT']
        else:
            ret = '%sx0' % context['CONFIG']['THUMBNAIL_MAX_WIDTH']
    else:
        ret = '%sx%s' % (
            context['CONFIG']['THUMBNAIL_MAX_WIDTH'],
            context['CONFIG']['THUMBNAIL_MAX_HEIGHT']
        )
    return ret
