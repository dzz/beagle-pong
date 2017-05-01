#version 330

uniform sampler2D motion_blur_buffer;
uniform float ball_x;
uniform float ball_english;

in vec2 uv;
out vec4 color;

//void main(void) {   
//
//    vec2 mod_uv = uv+vec2(1+(0.001*ball_x),0);
//    color = texture(motion_blur_buffer, mod_uv)*vec4(ball_english,1.0-ball_english,-1.0+ball_english,1.0)*0.99;
//}

void main(void) {   

    vec2 mod_uv = uv+vec2(1+(0.001*ball_x),0);
    color = texture(motion_blur_buffer, mod_uv)*vec4(ball_english,1.0-ball_english,-1.0+ball_english*ball_x,1.0)*0.99;
}
