package main

import (
	"image"
	"os"

	"image/color"
	_ "image/png"

	"github.com/gopxl/pixel/v2"
	"github.com/gopxl/pixel/v2/backends/opengl"
)

// SKYBLUE: pygame.Color = pygame.Color(113, 199, 245)
// BLACK: pygame.Color = pygame.Color(0, 0, 0)
// WHITE: pygame.Color = pygame.Color(255, 255, 255)
// BLUE: pygame.Color = pygame.Color(61, 139, 255)

func loadPicture(path string) (pixel.Picture, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()
	img, _, err := image.Decode(file)
	if err != nil {
		return nil, err
	}
	return pixel.PictureDataFromImage(img), nil
}

func run() {
	screenSize := pixel.R(0, 0, 960, 640)

	SKYBLUE := color.RGBA{113, 199, 245, 255}

	cfg := opengl.WindowConfig{
		Title:  "SFG by Sinoka",
		Bounds: screenSize,
		VSync:  true,
	}
	win, err := opengl.NewWindow(cfg)
	if err != nil {
		panic(err)
	}
	defer win.Destroy()

	// load image
	pic, err := loadPicture("./assets/img/player.png")
	if err != nil {
		panic(err)
	}

	// load sprite
	sprite := pixel.NewSprite(pic, pic.Bounds())

	win.Clear(SKYBLUE)
	sprite.Draw(win, pixel.IM.Moved(win.Bounds().Center()))

	for !win.Closed() {
		win.Update()
	}
}

func main() {
	opengl.Run(run)
}