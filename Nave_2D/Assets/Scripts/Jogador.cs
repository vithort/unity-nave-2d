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

    // Start is called before the first frame update
    void Start()
    {
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
    }
}
