from controller import *

menu = {
    'name' : 'root',
    'prompt' : 'Choose your destiny',
    'siblings' : [
            {   
                'name' : 'open',
                'prompt' : 'enter filename',
                'func' : open,
                'epilogue' : 'file opened'
            },
            {
                'name' : 'save',
                'prompt' : 'enter filename',
                'func' : save,
                'epilogue' : 'file saved'
            },
            {
                'name' : 'add',
                'prompt' : 'which figure you wanna add?(circle, rectangle)',
                'siblings' : [
                    {
                    'name' : 'circle',
                    'prompt' : 'enter x, y, radius',
                    'func' : draw_circle,
                    'epilogue' : 'circle added to image'
                    },
                    {
                    'name' : 'rectangle',
                    'prompt' : 'enter x, y, side1, side2',
                    'func' : draw_rectangle,
                    'epilogue' : 'circle added to image'
                    }
                ]
                },
            {
                'name' : 'show',
                'prompt' : "Here what we've got",
                'func' : show
            },
            {
                'name' : 'draw',
                'prompt' : 'start drawing..',
                'func' : draw
            },
            {
                'name' : 'exit',
                'prompt' : 'bye!',
                'func' : exit
            }
    ]
}