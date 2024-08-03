# Bored Cat

Bored Cat is an interactive application designed to entertain cats with various on-screen games and animations.

## Features

- Mouse Chase: A mouse that moves realistically across the screen, reacting to the cat's attempts to catch it.
- Laser Pointer: An interactive red dot that can be controlled by the mouse or move autonomously.
- Fish Tank: A virtual aquarium with different types of fish, bubbles, and interactive feeding.
- Yarn Ball: A physics-based yarn ball that unravels as it moves and can be interacted with via mouse.

## New in Version 1.1.0

- Improved physics and animations in all games
- Added user interaction in Yarn Ball and Fish Tank games
- Implemented pause/resume functionality
- Added sound effects (with mute option)
- Introduced basic settings customization

## Installation

1. Clone this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python -m bored_cat.main
   ```

## Usage

Launch the application and choose a game from the main menu. Each game is designed to capture a cat's attention and encourage play.

- Use the spacebar to pause/resume games
- Press 'M' to mute/unmute sound effects
- In Yarn Ball and Fish Tank, use the mouse to interact with game elements

## Configuration

Game settings can be customized by editing the `settings.json` file in the project root directory.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

### MIT License

Copyright (c) [2024] [DunamisMax]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.