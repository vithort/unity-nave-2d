using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Jogador : MonoBehaviour
{
    private float moverHorizontal;
    private float moverVertical;
    private Vector2 mover;
    private Rigidbody2D rb2d;
    private AudioSource audioSource;
    [SerializeField]
    private float velocidade;
    [SerializeField]
    private GameObject instanciarBombas;
    [SerializeField]
    private GameObject prefabBomba;
    private float controle;
    [SerializeField]
    private float atirarTempo;
    private float eixoXMin, eixoXMax;
    private float eixoYMin, eixoYMax;
    private float posicaoX, posicaoY;

    // Start is called before the first frame update
    void Start()
    {
        controle = 0f;
        eixoXMax = CameraPrincipal.LimitarDireitaX(transform.position);
        eixoXMin = CameraPrincipal.LimitarEsquerdaX(transform.position);
        eixoYMax = CameraPrincipal.LimitarParaCimaY(transform.position);
        eixoYMin = CameraPrincipal.LimitarParaBaixoY(transform.position);
        rb2d = GetComponent<Rigidbody2D>();
        audioSource = GetComponent<AudioSource>();
    }

    // Update is called once per frame
    void Update()
    {

    }

    void FixedUpdate()
    {
        moverHorizontal = Input.GetAxis("Horizontal");
        moverVertical = Input.GetAxis("Vertical");
        // Debug.Log(moverHorizontal);
        mover = new Vector2(moverHorizontal, moverVertical);
        rb2d.velocity = mover * velocidade;
        // Debug.Log(rb2d.velocity);
        if (Input.GetKeyDown(KeyCode.Space))
        {
            if (Time.time > controle)
            {
                controle = Time.time + atirarTempo;
                Instantiate(prefabBomba, instanciarBombas.transform.position, prefabBomba.transform.rotation);
                audioSource.Play();
            }
            
        }
        LimitarPosicaoJogador();
    }

    void LimitarPosicaoJogador()
    {
        posicaoX = rb2d.position.x; // transform.position.x;
        posicaoY = rb2d.position.y;
        posicaoX = Mathf.Clamp(posicaoX, eixoXMin, eixoXMax);
        posicaoY = Mathf.Clamp(posicaoY, eixoYMin, eixoYMax);

        if (posicaoX != transform.position.x)
        {
            rb2d.position = new Vector2(posicaoX, rb2d.position.y);
        }
        if (posicaoY != transform.position.y)
        {
            rb2d.position = new Vector2(rb2d.position.x, posicaoY);
        }
    }
}
