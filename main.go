package main

import (
	"image/color"

	"github.com/gopxl/pixel/v2"
	"github.com/gopxl/pixel/v2/backends/opengl"
)

// SKYBLUE: pygame.Color = pygame.Color(113, 199, 245)
// BLACK: pygame.Color = pygame.Color(0, 0, 0)
// WHITE: pygame.Color = pygame.Color(255, 255, 255)
// BLUE: pygame.Color = pygame.Color(61, 139, 255)

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

	win.Clear(SKYBLUE)

	for !win.Closed() {
		win.Update()
	}
}

func main() {
	opengl.Run(run)
}