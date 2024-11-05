window.onload = function() {
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');

    const character = {
        x: 400,
        y: 300,
        width: 50,
        height: 50,
        img: new Image(),
        speed: 5
    };
    character.img.src = 'static\img\character.png';

    const scenes = [
        { x: 50, y: 50, width: 200, height: 200, img: 'static\img\scene1.png', info: '어린 시절 이야기' },
        { x: 300, y: 50, width: 200, height: 200, img: 'static\img\scene2.png', info: '대학 시절 이야기' }
    ];

    scenes.forEach(scene => {
        const img = new Image();
        img.src = scene.img;
        img.onload = () => {
            ctx.drawImage(img, scene.x, scene.y, scene.width, scene.height);
        }
    });

    function drawCharacter() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        scenes.forEach(scene => {
            const img = new Image();
            img.src = scene.img;
            ctx.drawImage(img, scene.x, scene.y, scene.width, scene.height);
        });
        ctx.drawImage(character.img, character.x, character.y, character.width, character.height);
    }

    document.addEventListener('keydown', (e) => {
        switch(e.key) {
            case 'ArrowUp':
                character.y -= character.speed;
                break;
            case 'ArrowDown':
                character.y += character.speed;
                break;
            case 'ArrowLeft':
                character.x -= character.speed;
                break;
            case 'ArrowRight':
                character.x += character.speed;
                break;
        }
        drawCharacter();
    });

    drawCharacter();
}
