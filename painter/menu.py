menu = {
    'name' : 'root',
    'prompt' : 'What are you gonna do(open/save/add/show/draw/exit)',
    'siblings' : [
            {   
                'name' : 'open',
                'prompt' : 'enter filename',
                'func' : 'open_file'
            },
            {
                'name' : 'save',
                'prompt' : 'enter filename',
                'func' : 'save_file'
            },
            {
                'name' : 'add',
                'prompt' : 'which figure you wanna add?(circle, rectangle)',
                'siblings' : [
                    {
                    'name' : 'circle',
                    'prompt' : 'constructing circle:',
                    'func' : 'add_figure'
                    },
                    {
                    'name' : 'rectangle',
                    'prompt' : 'constructing rectangle',
                    'func' : 'add_figure'
                    }
                ]
                },
            {
                'name' : 'show',
                'prompt' : "Here what we've got\n",
                'func' : 'show'
            },
            {
                'name' : 'draw',
                'prompt' : 'start drawing..',
                'func' : 'draw'
            },
            {
                'name' : 'exit',
                'prompt' : 'bye!',
                'func' : 'exit'
            }
    ]
}