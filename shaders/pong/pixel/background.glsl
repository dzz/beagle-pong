#version 330

uniform sampler2D buffer;
uniform float time;

in vec2 uv;

void main(void) {
    gl_FragColor = vec4( 0.0, 0.0, 1.0, 1.0 );
}
