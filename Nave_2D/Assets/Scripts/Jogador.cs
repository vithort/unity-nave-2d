using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Jogador : MonoBehaviour
{
    private float moverHorizontal;
    private float moverVertical;
    private Vector2 mover;
    private Rigidbody2D rb2d;
    [SerializeField]
    private float velocidade;
    [SerializeField]
    private GameObject instanciarBombas;
    [SerializeField]
    private GameObject prefabBomba;
    private float controle;
    [SerializeField]
    private float atirarTempo;

    // Start is called before the first frame update
    void Start()
    {
        controle = 0f;
        rb2d = GetComponent<Rigidbody2D>();
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
            }
            
        }
    }
}
