using UnityEngine;
using System.Collections;

public class Projetil : MonoBehaviour
{
    [SerializeField]
    private float velocidade;
    private Rigidbody2D rb2d;


    // Start is called before the first frame update
    void Start()
    {
        rb2d = GetComponent<Rigidbody2D>();
        rb2d.velocity = transform.up * velocidade;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
