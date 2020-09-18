import torch
import torch.nn.functional as F


def DiffAugment(x, policy='', channels_first=True):
    if policy:
        if not channels_first:
            x = x.permute(0, 3, 1, 2)
        for p in policy.split(','):
            for f in AUGMENT_FNS[p]:
                x = f(x)
        if not channels_first:
            x = x.permute(0, 2, 3, 1)
        x = x.contiguous()
    return x



def augment_brightness(x):
    # to do

    return None


def augment_saturation(x):
    # to do
    return None


def augment_contrast(x):
    # to do
    return None


def augment_translation(x, ratio=0.125):
    # to do
    return None


def augment_cutout(x, ratio=0.5):
    # to do
    return None

AUGMENT_FNS = {
    'color': [augment_brightness, augment_saturation, augment_contrast],
    'translation': [augment_translation],
    'cutout': [augment_cutout],
}

